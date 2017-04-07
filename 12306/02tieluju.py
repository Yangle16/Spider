#-*- coding:utf-8 -*-
import requests ,time
from bs4 import BeautifulSoup

def get_info(url,desc):
    try:
        table = requests.get(url)
        c = BeautifulSoup(table.content, 'lxml')
        zhan_info = c.select("table.tb tr")
        # print zhan_info
        for x in range(2, len(zhan_info)):
            infos = zhan_info[x].find_all('td')
            st = ''
            for info in infos:
                st += info.text.encode('utf-8')
                st += ' '
            st += desc
            st += ','

            f.write(st)
            f.write('\n')

    except Exception as e:
        print e

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
        print station #

        url1 = url + chezhan_url1[2:]
        url2 = url + chezhan_url2[2:]
        print url1, url2

        with open('02station_info.csv', 'a+') as f:
            f.write(station.encode('utf-8') + '\n')
            get_info(url1,' =>车站')
            f.write('\n')
            time.sleep(5)

            get_info(url2,' =>乘降所')
            f.write('--' * 50 + '\n')
            time.sleep(5)



