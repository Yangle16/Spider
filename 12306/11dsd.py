#-*- coding:utf-8 -*-
import requests, time, json, urllib3
from bs4 import BeautifulSoup

requests.packages.urllib3.disable_warnings()

"""
查询全国全部代售点
"""

def fetch_provinces():
    url = "https://kyfw.12306.cn/otn/userCommon/allProvince"

    try:
        s = requests.get(url, verify=False) # 验证要关闭，不然失败
    except Exception, e:
        print "fetch province. " + url
        raise e

    j = json.loads(s.content)
    return j["data"]

def fetch_data(url, province, fd):
    try:
        s = requests.get(url, params={"province":province, "city":"", "county":""}, verify=False)
    except Exception as e:
        print "requests url fail.", url, province.encode('utf-8')
        return

    datas = json.loads(s.content)

    for data in datas["data"]["datas"]:
        out = u""
        out += data["province"]
        out += u" " + data["city"]
        out += u" " + data["county"]
        out += u" " + data["agency_name"]
        out += u" " + data["address"]
        out += u" " + data["windows_quantity"]
        start = data["start_time_am"]
        end = data["stop_time_pm"]
        out += u" " + start[:2] + ":" + start[2:] + "-" + end[:2] + ":" + end[2:]

        s = out.encode("utf-8")
        fd.write(s)
        fd.write('\n')
        print s

if __name__ == "__main__":
    provs = fetch_provinces()

    url = "https://kyfw.12306.cn/otn/queryAgencySellTicket/query"

    with open('11dsd.txt', 'w') as fd:
        for prov in provs:
            fetch_data(url, prov["chineseName"], fd)
            time.sleep(5)