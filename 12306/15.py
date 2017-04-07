#-*- coding:utf-8 -*-
import datetime, time, json, requests

requests.packages.urllib3.disable_warnings()

"""
获取任意有效两个车站的车票信息
"""

# 票价
def fetch_price(t, strat, end, train_no, seat_types, code, f2, src_name, des_name):
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
    f2.write(src_name + ' => ' + des_name)
    f2.write(s)
    f2.write('\n')
    print s

# 列车时刻表
def fetch_stations(t, strat, end, train_no, code, f1):
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
        f1.write('\n')
        f1.write(s)
        print s
    f1.write('\n')

# 车次信息
def fetch_data(t, start, end, f1, f2, existed_codes):
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

        is_fetch_station = False

        if no in existed_codes:
            if (src_name, des_name) in existed_codes[no]:
                continue
            else:
                existed_codes[no].add((src_name, des_name))
        else:
            is_fetch_station = True
            existed_codes[no] = [(src_name, des_name)]

        time.sleep(2)
        print '\n', src_name, '=>', des_name
        fetch_price(t, info["from_station_no"], info["to_station_no"], no, info["seat_types"], code, f2, src_name, des_name)

        if is_fetch_station:
            time.sleep(2)
            fetch_stations(t, start, end, no, code, f1)

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

    for i in range(1, len(stations)):
        station = stations[i].split('|')
        out = station[1] + ' ' + station[2] + '\n'
        with open("15.station_code.txt", 'a') as f:
            f.write(out.encode('utf-8'))

    return stations

# 对列车存在线路存储
def del_and_store(existed_codes):
    result = set()
    with open("15.routes.txt",'w') as f:
        for code in existed_codes:
            routes = existed_codes[code]
            for route in routes:
                if route not in result:
                    result.add(route)
                    out = route[0] + ' ' + route[1] + '\n'
                    f.write(out.encode('utf-8'))

# 获取车站代号、进行始发和终点站迭代、调用车次函数
def fetch_trains_static_info(existed_codes):
    fetch_stations_code()
    with open('15.station_code.txt', 'r') as fd:
        stations = fd.read().decode('utf-8')
        stations2 = stations.split('\n')

    size = len(stations2)
    print size
    with open('15.train_code.txt','a+') as f1:
        with open('15.train_price.txt', 'a+') as f2:
            for i in range(0, size-1):
                for j in range(i+1,size):
                    t = (datetime.datetime.now()+datetime.timedelta(days=3)).strftime("%Y-%m-%d")
                    src = stations2[i].split(' ')[1]
                    des = stations2[j].split(' ')[1]

                    time.sleep(2)
                    print stations2[i].split(' ')[0], stations2[j].split(' ')[0]
                    fetch_data(t, src, des, f1, f2, existed_codes)
    return existed_codes


if __name__ == "__main__":
    existed_codes = {}
    fetch_trains_static_info(existed_codes)
    del_and_store(existed_codes) # 查询完毕，进行线路存储