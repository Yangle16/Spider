#-*- coding:utf-8 -*-
import json

with open('15.station_code.txt', 'rb') as f5:
    a = f5.read().split('\r\n')
    for i in a:
        b = i.split(' ')
        # print b
        c = b[0]
        d = b[1]

        print  '{' + c + ':' + d + '}' + ','
