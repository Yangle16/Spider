#-*- coding:utf-8 -*-
import urllib, urllib2, requests, re, cookielib
import os, time
from bs4 import BeautifulSoup
from pymongo import MongoClient, errors
from selenium import webdriver


url = 'https://mm.taobao.com/json/request_top_list.htm?page='

page_max = 50

headers = {
    'referer':'https://mm.taobao.com/',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}

agents = {}

poxy = {}


def page_url():
    for i in range(13, page_max+1):
        page_url = url + str(i)
        print page_url

        mm_list(page_url, i)

def mm_list(page_url, num):
    mm_num = (num-1) * 10 + 1
    page = requests.get(page_url, headers= headers, timeout=10).text
    links = BeautifulSoup(page, 'lxml').select('a.lady-name')
    for i in range(0, len(links)):
        link = 'https:' + links[i]['href']
        drive = webdriver.PhantomJS()
        drive.get(link)
        time.sleep(1)

        mm_name = drive.find_element_by_css_selector('div.mm-p-model-info-left-top > dl > dd > a').text

        # 查找模特个人域名地址
        try:
            mm_url = drive.find_element_by_css_selector('#J_MmInfo > div.mm-p-middle.mm-p-sheShow > div.mm-p-info.mm-p-domain-info > ul > li > span').text
        except Exception as e:
            print e
            print u'模特域名获得失败：', mm_num, mm_name, link
            failure = str(mm_num) +  mm_name + link
            with open('failure_mm.txt', 'a+') as f2:
                f2.write(failure.encode('utf-8') + '\n')
            continue
        mm_domain = 'https:' + mm_url
        print mm_num, mm_name, mm_domain
        time.sleep(1)

        # 进入模特个人空间，图片链接会全部在源代码中
        # drive.get(mm_domain) # 这里卡主啦，一直在加载图片，解决跳过问题
        # time.sleep(2)
        # imgs = drive.find_element_by_css_selector('img')['src']

        req = requests.get(mm_domain, timeout=10).text
        imgs = BeautifulSoup(req, 'lxml').select('img')
        print mm_num, mm_name, u"图片页,", len(imgs), u'张图片'

        push_info(link, mm_num, mm_name)

        img_urls = []
        for j in range(0, len(imgs)):
            try:
                img_url = 'https:' + imgs[j]['src']
                img_urls.append(img_url)
                if img_url.startswith('https://img.alicdn.com/imgextra/'):
                    print img_url
                    img_download(img_url, mm_name, mm_num)
            except Exception as e2:
                print e2
                continue

        push_imgs(mm_url, img_urls)

        mm_num += 1


def push_info(mm_url, mm_num, mm_name):
    con = MongoClient()
    db = con['taobao_mm']
    clc = db['mm_info']
    try:
        clc.insert({'_id': mm_url, '序号':mm_num, '模特': mm_name})
        print u'模特数据入库成功！'
    except errors.DuplicateKeyError as e:
        print u'_^^_ 模特数据插入失败，已有数据！'
        pass

    con.close()

def push_imgs(mm_url, img_urls):
    con = MongoClient()
    db = con['taobao_mm']
    clc = db['mm_img']
    try:
        clc.insert({'_id': mm_url,'img_urls': img_urls})
        print u'图片数据入库成功！'
    except errors.DuplicateKeyError as e:
        print u'_^^_ 图片数据插入失败，已有数据！'
        pass

    con.close()


def mkdir(mm_name, mm_num):
    dir_path = str(mm_num) + mm_name
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
        return dir_path
    else:
        return dir_path

def img_download(img_url, mm_name, mm_num):
    dir_path = mkdir(mm_name, mm_num)
    img_name = dir_path + '/' + img_url.split('/')[-1].split(' ')[0] + '.jpg'
    if not os.path.exists(img_name):
        try:
            img = requests.get(img_url, headers= headers, timeout=5).content
            with open(img_name,'wb') as f:
                    f.write(img)
        except Exception as e:
            print e


if __name__ == "__main__":
    page_url()

    """模特编号，链接去重待完善！！2017年03月26日(星期日)"""