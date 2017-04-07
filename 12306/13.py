#-*- coding:utf-8 -*-
import datetime, requests, json, time

requests.packages.urllib3.disable_warnings()

"""
两个车站间，车票信息查询（车票、票价、时刻表）
"""

# 列车时刻表
def fetch_stations(t, strat, end, train_no, f):
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
        f.write('\n')
        f.write(s)
        print s
    f.write('\n')

# 票价查询
def fetch_price(t, strat, end, train_no, seat_types, f):
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
    f.write(s)
    f.write('\n')
    print s

# 车次信息
def fetch_data(t, start, end, f):
    # https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2017-03-15&leftTicketDTO.from_station=SZQ&leftTicketDTO.to_station=WHN&purpose_codes=ADULT
    url = "https://kyfw.12306.cn/otn/leftTicket/query?"
    params = "leftTicketDTO.train_date=" + t + "&leftTicketDTO.from_station=" + start + "&leftTicketDTO.to_station=" + end + "&purpose_codes=ADULT"
    try:
        s = requests.get(url,params = params.encode('utf-8'), verify=False)
    except Exception as e:
        print "requests url fail. ", url
        return

    datas = json.loads(s.content)
    # print datas["data"]

    # if 'secretStr' not in datas["data"]:
    #     print "no train", t, start.encode('utf-8'), end.encode('utf-8')
    #     return

    for data in datas["data"]:
        # print data['queryLeftNewDTO']
        info = data['queryLeftNewDTO']
        out = "--"*50 + '\n'
        out += info["from_station_name"]
        out += ' ' + info["end_station_name"]
        out += ' ' + info["station_train_code"]
        out += '\n' + info["swz_num"]
        out += ' ' + info["tz_num"]
        out += ' ' + info["zy_num"]
        out += ' ' + info["ze_num"]
        out += ' ' + info["gr_num"]
        out += ' ' + info["rw_num"]
        out += ' ' + info["yw_num"]
        out += ' ' + info["rz_num"]
        out += ' ' + info["yz_num"]
        out += ' ' + info["wz_num"]
        out += ' ' + info["qt_num"]

        s = out.encode('utf-8')
        f.write(s)
        f.write('\n')
        print s

        time.sleep(2)
        fetch_price(t, info["from_station_no"], info["to_station_no"], info["train_no"], info["seat_types"], f)

        time.sleep(2)
        fetch_stations(t, start, end, info["train_no"], f)

        time.sleep(2)


# 主函数，先需给定两个车站代号
if __name__ == "__main__":
    with open("13.txt", 'w') as f:
        fetch_data((datetime.datetime.now() + datetime.timedelta(days=3)).strftime("%Y-%m-%d"), "SZQ", "WHN", f)
