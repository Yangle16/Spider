#-*- coding:utf-8 -*-
import datetime, time, json, requests, urllib

requests.packages.urllib3.disable_warnings()

"""
获取车次正晚点信息
"""

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

    print s.content.strip().decode('gbk')


if __name__ == "__main__":
    train_code = raw_input('请输入车次：')
    station_name = raw_input('请输入到达站：')

    fetch_schedule(train_code, station_name, False)

