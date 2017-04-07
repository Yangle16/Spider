#-*- coding:utf-8 -*-
import datetime, time, json, requests, urllib

requests.packages.urllib3.disable_warnings()

"""
获取车次正晚点信息
"""

def load_resoure():
    arrives = {}
    for i in range(0, 24):
        arrives[i] = []

    with open('16.train_time_table.txt', 'r') as f:
        new_train_line = 0
        code = ''
        for line in f.xreadlines():
            new_train_line += 1
            if line.startswith('-'):
                new_train_line = 0
            elif new_train_line == 1:
                code = line[:line.find('(')]
            elif line == '\n':
                continue
            else:
                params = line.split(' ')
                name = params[1]
                arrive = params[2]
                if not arrive.startswith('-'):
                    t = datetime.datetime.strftime(arrive, '%H:%M')
                    arrives[t.hour].append((code, name))

    return arrives

def fetch_schedule(train_code, station_name, depart):

    url = 'http://dynamic.12306.cn/mapping/kfxt/zwdcx/LCZWD/cx.jsp?'
    # http://dynamic.12306.cn/mapping/kfxt/zwdcx/LCZWD/cx.jsp?cz=%CE%E4%BA%BA&cc=G1002&cxlx=0&rq=2017-03-18&czEn=-E6-AD-A6-E6-B1-89&tp=1489808562439

    params = {
        'cz':station_name,
        'cc':train_code,
        'cxlx':'1' if depart else '0',
        'rq':datetime.datetime.now().strftime('%Y-%m-%d'),
        'czEn':urllib.quote(station_name).replace('%','-'),
        'tp':int(time.time()* 1000),
    }
    headers = {
        'Referer': 'http://dynamic.12306.cn/mapping/kfxt/zwdcx/LCZWD/CCCX.jsp',
        'User-Agent': 'Mozilla/5.0(WindowsNT10.0;WOW64) AppleWebKit/537.36(KHTML, likeGecko) Chrome/56.0.2924.87Safari/537.36',
    }

    try:
        s = requests.get(url, params=params, headers=headers)
    except Exception as e:
        print "request fail. " + url
        raise e

    # print s.content.strip().decode('gbk')
    return s.content.strip().decode('gbk')


if __name__ == "__main__":
    arrives = load_resoure()
    while True:
        t = datetime.datetime.now()
        curs = arrives[(t.hour + 2)%24]
        for cur in curs:
            time.sleep(2)
            result = fetch_schedule(cur[0], cur[1], 0)
            if result.startswith(u"预计"):
                print result.encode('utf-8')
