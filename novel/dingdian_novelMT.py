#-*- coding:utf-8 -*-
import os
import time
import threading
import multiprocessing
from dingdian_novelDB import MogoQueue
from bs4 import BeautifulSoup
import requests, cookielib


SLEEP_TIME = 1

def dingdian_crawler(max_threads=10):
    crawl_queue = MogoQueue('dingdian_novel', 'crawl_queue')  #这个是我们获取URL的队列
    chapter_queue = MogoQueue('dingdian_novel', 'chapter_queue')
    spider_queue = MogoQueue('dingdian_novel', 'crawl_queue')  # 调用数据库

    url = 'http://www.23us.com/quanben/1'

    headers = {
        'Referer': 'http://www.23us.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }

    s = requests.Session()
    s.cookies = cookielib.LWPCookieJar(filename='cookies4')

    def num_page():
        page = s.get(url, headers=headers).text.encode('iso-8859-1').decode('gb18030')
        # print page
        num_page = int(BeautifulSoup(page, 'lxml').select('#pagelink > a.last')[0].text)
        print u'共有', num_page, u'页'
        for i in range(1, num_page + 1):
            index(i)
            print u'正在', i, u'页下载，', u'共', num_page, u'页'

    def index(pn):
        page_url = 'http://www.23us.com/quanben/' + str(pn)
        page = s.get(page_url, headers=headers).text.encode('iso-8859-1').decode('gb18030')
        # print page
        trs = BeautifulSoup(page, 'lxml').select('tr[bgcolor="#FFFFFF"]')
        # print trs
        if pn == 1:
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

            spider_queue.push(novel_url, name)  # 小说地址、名称存入数据库

            novel_page()
            num_novel += 1
            print u'下载第', num_novel, u'部小说', name

    def novel_page():
        while True:
            try:
                url = crawl_queue.pop()
                print(url)
            except KeyError:
                print('队列没有数据')
                break
            else:
                chapter_urls = []
                page = s.get(url).text
                name = crawl_queue.pop_novel(url)

                urls = BeautifulSoup(page, 'lxml').select('td.L > a')
                name2 = BeautifulSoup(page.encode('iso-8859-1').decode('gb18030'), 'lxml').select('h1')[0].text.split(' ')[0]

                for j in range(0, len(urls)):
                    print u'总共', len(urls) + 1, u'章，', u'这是', j + 1, u'章'
                    chapter_url = url + urls[j]['href']
                    chapter_urls.append(chapter_url)
                    try:
                        chapter_name = urls[j].text.encode('iso-8859-1').decode('gb18030')
                        print chapter_url

                        novel = name2 + '.txt'
                        with open(novel, 'a+') as f:
                            chapter(chapter_url, url, chapter_name, f)
                    except Exception as e:
                        print e
                    time.sleep(0)

                chapter_queue.push_chapterurl(name, chapter_urls)
                print u'插入数据库成功'
                crawl_queue.complete(url) ##设置为完成状态


    def chapter(chapter_url, url, chapter_name, f):
        headers2 = {
            'Host': 'www.23us.com',
            'Referer': url,
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

    threads = []
    while threads or crawl_queue:
        """
        这儿crawl_queue用上了，就是我们__bool__函数的作用，为真则代表我们MongoDB队列里面还有数据
        threads 或者 crawl_queue为真都代表我们还没下载完成，程序就会继续执行
        """
        for thread in threads:
            if not thread.is_alive(): ##is_alive是判断是否为空,不是空则在队列中删掉
                threads.remove(thread)
        while len(threads) < max_threads or crawl_queue.peek(): ##线程池中的线程少于max_threads 或者 crawl_qeue时
            thread = threading.Thread(target=num_page()) ##创建线程
            thread.setDaemon(True) ##设置守护线程
            thread.start() ##启动线程
            threads.append(thread) ##添加进线程队列
        time.sleep(SLEEP_TIME)

def process_crawler():
    process = []
    num_cpus = multiprocessing.cpu_count()
    print u'将会启动进程数为：', num_cpus
    for i in range(num_cpus):
        p = multiprocessing.Process(target=dingdian_crawler) ##创建进程
        p.start() ##启动进程
        process.append(p) ##添加进进程队列
    for p in process:
        p.join() ##等待进程队列里面的进程结束

if __name__ == "__main__":

    process_crawler()
