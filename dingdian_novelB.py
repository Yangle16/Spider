#-*- coding:utf-8 -*-
import urllib, urllib2, requests, cookielib
import time
from bs4 import BeautifulSoup


url = 'http://www.23us.com/quanben/1'

headers = {
    'Referer':'http://www.23us.com/',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}

s = requests.Session()
s.cookies = cookielib.LWPCookieJar(filename='cookies4')


def num_page():
    page = s.get(url, headers=headers).text.encode('iso-8859-1').decode('gb18030')
    # print page
    num_page = int(BeautifulSoup(page, 'lxml').select('#pagelink > a.last')[0].text)
    print u'共有', num_page, u'页'
    for i in range(1, num_page+1):
        index(i)
        print u'正在', i, u'页下载，', u'共', num_page, u'页'

def index(pn):
    page = s.get(url, headers=headers).text.encode('iso-8859-1').decode('gb18030')
    # print page
    trs = BeautifulSoup(page, 'lxml').select('tr[bgcolor="#FFFFFF"]')
    # print trs
    if pn == 0:
        num_novel = 0
    else:
        num_novel = (pn - 1) * 30

    for i in range(0, len(trs)):
        txt = str(trs[i])
        # print txt
        # fenlei = BeautifulSoup(txt, 'lxml').select('span.s1')[0].text
        name = BeautifulSoup(txt, 'lxml').select('td')[0].select('a')[1].text
        novel_url = BeautifulSoup(txt, 'lxml').select('td')[0].select('a')[1]['href']
        author = BeautifulSoup(txt, 'lxml').select('td')[2].text
        update = BeautifulSoup(txt, 'lxml').select('td')[4].text
        status = BeautifulSoup(txt, 'lxml').select('td')[5].text

        print novel_url
        # print fenlei, name, author, update, status
        num_novel += 1
        novel = str(num_novel) + '.' + name + '.txt'
        with open(novel,'w') as f:
            novel_page(novel_url, f)

        print u'下载第', num_novel, u'部小说', name


def novel_page(url_all, f):
    page = s.get(url_all).text

    urls = BeautifulSoup(page, 'lxml').select('td.L > a')

    for j in range(0, len(urls)):
        print u'总共', len(urls) + 1, u'章，', u'这是', j+1, u'章'
        chapter_url = url_all + urls[j]['href']
        try:
            chapter_name = urls[j].text.encode('iso-8859-1').decode('gb18030')
            print chapter_url

            chapter(chapter_url, url_all, chapter_name, f)
        except Exception as e:
            print e

        time.sleep(0)


def chapter(chapter_url, url_all, chapter_name, f):
    headers2 = {
        'Host': 'www.23us.com',
        'Referer': url_all,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

    try:
        page = s.get(chapter_url, headers=headers2, timeout=10).text.encode('iso-8859-1').decode('gb18030')
        # print page
        txt = BeautifulSoup(page, 'lxml').select('#contents')[0].text
        print chapter_name
        # print txt.encode('iso-8859-1').decode('gb18030')

        f.write(u''.join(chapter_name).encode('utf-8'))
        f.write('\n')
        f.write(u''.join(txt).encode('utf-8'))
        f.write('\n')
        f.write('\n')
    except Exception as e:
        print e


s.cookies.save()

if __name__ == "__main__":
    num_page()
