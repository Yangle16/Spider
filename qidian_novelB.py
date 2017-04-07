#-*- coding:utf-8 -*-
import urllib2,urllib,re,os,requests,time

# url = 'http://a.qidian.com/'

# 分页
# http://a.qidian.com/?size=-1&sign=-1&tag=-1&chanId=-1&subCateId=-1&orderId=&update=-1&page=2&month=-1&style=1&action=-1&vip=-1
# http://a.qidian.com/?size=-1&sign=-1&tag=-1&chanId=-1&subCateId=-1&orderId=&update=-1&page=3&month=-1&style=1&action=-1&vip=-1
# 分析发现，page=2，page=3，在变化，其他没有
# 爬取100页小说信息，起点目前有28100页

def filter(text):
    # content = re.compile('^\s*|\s*$',re.S)
    # content2 = re.findall(content,text)
    content = text.replace('\r\n','')
    content2 = content.replace(' ','')
    return content2

num = 1  # 序号

header = {
    'Referer':'http://www.qidian.com/',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}

for x in range(1,28101):
    url = 'http://a.qidian.com/?size=-1&sign=-1&tag=-1&chanId=-1&subCateId=-1&orderId=&update=-1&page='+str(x)+'&month=-1&style=1&action=-1&vip=-1'
    # url = 'http://a.qidian.com/'
    # print url
    print u"正在下载第" + str(x) + u"页内容，请稍等！"

    try:
        html = urllib2.urlopen(url,context=header,timeout=5).read()
        # print html
    except Exception as e:
        print e
        continue

    # <h4><a href="//book.qidian.com/info/3683064" target="_blank" data-eid="qd_C40" data-bid="3683064">崩坏星河</a></h4>

    # 作品 作者 分类 状态 简介 字数
    try:
        reg = re.compile(r'data-eid="qd_B58" .*?>(.*?)</a></h4>.*?data-eid="qd_B59" .*?>(.*?)</a>.*?data-eid="qd_B61">(.*?)</a>.*?<span >(.*?)</span>.*?class="intro">(.*?)</p>.*?class="update"><span >(.*?)</span>',re.S)
        iterms = re.findall(reg, html)

        # 加一个作品网址
        novel_reg = re.compile('<div class="book-mid-info">.*?href="(.*?)"', re.S)
        novel_urls = re.findall(novel_reg, html)

        # print len(iterms)
    except Exception as e:
        print e
        continue

    for (i,y) in zip(iterms,novel_urls):
        # print '作品 ' + i[0] + '\t' + '作者 ' + i[1] + '\t' + '分类 ' + i[2] + '\t' + '状态 ' + i[3] + '\t' + '简介 ' + i[4] + '\t' + '字数 ' + i[5] + '\t' + '\n'

        text = filter(i[4])
        # print text
        novel_url = 'http:' + y

        m = str(num)+'\t' + '作品:' + '<<' + i[0] + '>>' + '\t' + '作者:' + i[1] + '\t' + '分类:' + i[2] + '\t' + '状态:' + i[3] + '\t' + '字数:' + i[5] + '\t' + '网址:' + novel_url + '\t' + '简介:' + text + '\n'
        title = "novel_info" + '.csv'
        w = file(title, 'a+')
        w.write(m)
        w.close()
        num += 1

    time.sleep(0)

print u"全部小说作品信息下载完毕！尽情阅览！(^_^)"

exit()