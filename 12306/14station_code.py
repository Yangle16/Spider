#-*- coding:utf-8 -*-
import requests

requests.packages.urllib3.disable_warnings()

"""
12306车站代号获取
"""

# 车站代号
def fetch_station(f):
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
        f.write(out.encode('utf-8'))

if __name__ == "__main__":
    with open("14.txt", 'w') as f:
        fetch_station(f)