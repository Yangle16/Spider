#-*- coding:utf-8 -*-
import requests ,time
from bs4 import BeautifulSoup

if __name__ == "__main__":
    url = "http://www.12306.cn/mormhweb/kyyyz/"
    s = requests.get(url)
    b = BeautifulSoup(s.content, 'lxml')
    tieluju = b.select("#secTable > tbody > tr > td") # 铁路局
    chezhan = b.select("#mainTable td.submenu_bg > a") # 车站

    for i in range(0,len(tieluju)):
        chezhan_url1 = chezhan[i * 2]['href']
        chezhan_url2 = chezhan[i * 2 + 1]['href']
        station = tieluju[i].text
        print station #, chezhan_url1, chezhan_url2
        with open('station_info.csv', 'a+') as f:
            f.write(station.encode('utf-8')+'\n')
        url1 = url + chezhan_url1[2:]
        url2 = url + chezhan_url2[2:]
        print url1, url2
        try:
            table = requests.get(url1)
            c = BeautifulSoup(table.content, 'lxml')
            # print c
            zhan_info = c.select("table.tb > tbody > tr > td")

            # print zhan_info
            print len(zhan_info)
            if len(zhan_info) == 0:
                zhan_info = c.select("table.tb > tr > td")
                for x in range(0, len(zhan_info)):
                    info = zhan_info[x].text
                    print info
                    with open('station_info.csv','a+') as f:
                        f.write(info.encode('utf-8')+'\n')
            else:
                zhan_info = c.select("table.tb > tbody > tr > td")
                for j in range(0, len(zhan_info)):
                    info = zhan_info[j].text
                    print info
                    with open('station_info.csv', 'a+') as f:
                        f.write(info.encode('utf-8')+'\n')

        except Exception as e:
            print e

        time.sleep(5)
