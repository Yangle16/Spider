#-*- coding:utf-8 -*-
import datetime, time, json, requests, re

requests.packages.urllib3.disable_warnings()

"""
获取所有路线信息
"""

def fetch_all_train(f):
    url = 'https://kyfw.12306.cn/otn/queryTrainInfo/getTrainName?date=' + t
    try:
        s = requests.get(url, verify=False)
    except Exception as e:
        print "fetch stations fail. " + url
        raise e
    train_str = json.loads(s.content.decode('utf-8'))

    trains = train_str['data']
    # {"station_train_code": "0000(沈阳-北京)", "train_no": "120000421606"}

    for i in range(0, len(trains)):
        station = trains[i]
        out = station["station_train_code"] + ' ' + station["train_no"] + '\n'
        f.write(out.encode('utf-8'))


def fetch_info(f2):
    """
    0000(沈阳-北京) 120000421606
    0000(通辽-上海) 16000043100C
    D1(北京-沈阳) 24000000D10R
    G1(北京南-上海虹桥) 24000000G10D
    """
    text = f2.read().split('\n')
    to_go = []
    for t in text:
        req = re.compile(r'.*?\((.*?)-(.*?)\)')
        to_go_r = re.findall(req, t)
        to_go.append(to_go_r)
        # print to_go[0][0] + ' ' + to_go[0][1] + '\n'
    # print to_go
    return to_go



# 票价
def fetch_price(t, strat, end, train_no, seat_types, code, f4, src_name, des_name):
    # https://kyfw.12306.cn/otn/leftTicket/queryTicketPrice?train_no=6i00000G7806&from_station_no=01&to_station_no=04&seat_types=O9MO&train_date=2017-03-15
    url = "https://kyfw.12306.cn/otn/leftTicket/queryTicketPrice?"

    params = "train_no=" + train_no + "&from_station_no=" + strat + "&to_station_no=" + end + "&seat_types=" + seat_types + "&train_date=" + t

    try:
        s = requests.get(url, params=params.encode('utf-8'), verify=False)
    except Exception as e:
        print "fetch price fail. " + url
        raise e

    prices = json.loads(s.content)
    price = prices["data"]

    out = '\n'
    if "A9" in price:
        out += price["A9"]
    else:
        out += " --"
    if "P" in price:
        out += " " + price["P"]
    else:
        out += " --"
    if "M" in price:
        out += " " + price["M"]
    else:
        out += " --"
    if "O" in price:
        out += " " + price["O"]
    else:
        out += " --"
    if "A6" in price:
        out += " " + price["A6"]
    else:
        out += " --"
    if "A4" in price:
        out += " " + price["A4"]
    else:
        out += " --"
    if "A3" in price:
        out += " " + price["A3"]
    else:
        out += " --"
    if "A1" in price:
        out += " " + price["A1"]
    else:
        out += " --"
    if "WZ" in price:
        out += " " + price["WZ"]
    else:
        out += " --"
    if "MIN" in price:
        out += " " + price["MIN"]
    else:
        out += " --"

    s = out.encode('utf-8')
    f4.write(src_name + ' => ' + des_name)
    f4.write('  ' + code)
    f4.write(s)
    f4.write('\n')
    print s

# 列车时刻表
def fetch_stations(t, strat, end, train_no, code, f3):
    # https://kyfw.12306.cn/otn/czxx/queryByTrainNo?train_no=6500000T9608&from_station_telecode=SZQ&to_station_telecode=WCN&depart_date=2017-03-15
    url = "https://kyfw.12306.cn/otn/czxx/queryByTrainNo?"

    params = "train_no=" + train_no + "&from_station_telecode=" + strat + "&to_station_telecode=" + end + "&depart_date=" + t

    try:
        s = requests.get(url, params=params.encode('utf-8'), verify=False)
    except Exception as e:
        print "fetch stations fail. " + url
        raise e

    stations = json.loads(s.content)

    for station in stations["data"]["data"]:
        out = ''
        out += station["station_no"]
        out += ' ' + station["station_name"]
        out += ' ' + station["arrive_time"]
        out += ' ' + station["start_time"]
        out += ' ' + station["stopover_time"]

        s = out.encode("utf-8")
        f3.write('\n')
        f3.write(code + '  ')
        f3.write(s)
        print s
    f3.write('\n')

# 车次信息
def fetch_data(t, start, end, f3, f4):
    # https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2017-03-15&leftTicketDTO.from_station=SZQ&leftTicketDTO.to_station=WHN&purpose_codes=ADULT
    url = "https://kyfw.12306.cn/otn/leftTicket/query?"
    params = "leftTicketDTO.train_date=" + t + "&leftTicketDTO.from_station=" + start + "&leftTicketDTO.to_station=" + end + "&purpose_codes=ADULT"
    try:
        s = requests.get(url, params=params.encode('utf-8'), verify=False)
    except Exception as e:
        print "requests url fail. ", url
        return

    datas = json.loads(s.content)

    # if "datas" not in datas["data"]:
    #     print "no train", t, start.encode('utf-8'), end.encode('utf-8')
    #     return

    for data in datas["data"]:
        time.sleep(2)
        info = data['queryLeftNewDTO']

        code = info["station_train_code"]
        src_name = info["from_station_name"].encode('utf-8')
        des_name = info["end_station_name"].encode('utf-8')
        no = info["train_no"]

        # is_fetch_station = False

        time.sleep(2)
        print '\n', src_name, '=>', des_name, code
        fetch_price(t, info["from_station_no"], info["to_station_no"], no, info["seat_types"], code, f4, src_name, des_name)

        time.sleep(2)
        fetch_stations(t, start, end, no, code, f3)

# 车站代号
def fetch_stations_code():
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9001'
    try:
        s = requests.get(url, verify=False)
    except Exception as e:
        print "fetch stations fail. " + url
        raise e
    station_str = s.content.decode('utf-8')

    stations = station_str.split('@')

    with open("16.station_code.txt", 'w') as f:
        for i in range(1, len(stations)):
            station = stations[i].split('|')
            out = '{' + '\"'+ station[1] +'\"' + ':' + '\"'+ station[2] +'\"' + '}'+ ','
            f.write(out.encode('utf-8'))

def to_go_code(f5):
    a = f5.read()
    station_codes = json.loads(a)
    # print station_codes

    start = []
    end = []
    print len(to_go)
    print to_go[8775] # 最后一个为空值
    for i in range(0, len(to_go)-1):
        a = to_go[i][0][0]
        b = to_go[i][0][1]
        print i
        for x in station_codes:
            # print x.keys()[0]
            if x.keys()[0].encode('utf-8') == a:
                start.append(x.values()[0])
                # print start[i]
                for y in station_codes:
                    if y.keys()[0].encode('utf-8') == b:
                        end.append(y.values()[0])
                        # print end[i]

    return start, end

if __name__ == "__main__":
    t = (datetime.datetime.now() + datetime.timedelta(days=3)).strftime("%Y-%m-%d")

    with open("16.all_train.txt", 'w') as f:
        fetch_all_train(f)

    with open("16.all_train.txt", 'r') as f2:
        to_go = fetch_info(f2)

        fetch_stations_code()
        with open('16.station_code2.txt', 'r') as f5:
            start, end = to_go_code(f5)

            for j in range(0,len(start)):
                with open('16.train_time_table.txt', 'a+') as f3:
                    with open('16.train_price.txt', 'a+') as f4:
                         fetch_data(t, start[j], end[j], f3, f4)