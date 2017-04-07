#-*- coding:utf-8 -*-
import urllib2,urllib,re,os,requests,time,sys


def mkDir(dirName):
    dirpath = os.path.join(sys.path[0], dirName)
    if not os.path.exists(dirpath):
        os.mkdir(dirpath)
    return dirpath

url = raw_input('Please input course url:')
files = "MaiziEDU_" + raw_input('Please create store dir:')
dirpath = mkDir(files)

header = {
    'Referer':'http://m.maiziedu.com/',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}

page = requests.get(url, headers=header).text

# <li><a href="/course/751-10786/"><span>05:52</span>1.pandas课程介绍</a></li>
req1 = re.compile(r'<ol>(.*?)</ol>', re.S)
urls = re.findall(req1,page)

req = re.compile(r'<li><a href="(.*?)"><span>.*?</span>(.*?)</a></li>', re.S)
info = re.findall(req, urls[0])
# print info
for i in info:
    course_url = i[0]
    course_name = i[1]
    # print course_url
    # print course_name.encode('utf-8')

    url = 'http://m.maiziedu.com'+ course_url
    print url
    print u"正在下载，请稍等！"

    try:
        html = urllib2.urlopen(url,context=header,timeout=120).read()
        # print html
    except Exception as e:
        print e
        print u'下载失败: ' + url
        continue

# < section class ="course-banner" >
# < video autoplay controls = "controls" preload = "" poster = "" src = "http://newoss.maiziedu.com/python12306/python12306-36.mp4" >
# < source src = "http://newoss.maiziedu.com/python12306/python12306-36.mp4" type = "video/mp4" >
# < / video >
# < h2 > 12306商业爬虫课程总结 < / h2 >
# < / section >

    try:
        reg = re.compile(r'<section class="course-banner">.*?src="(.*?)">',re.DOTALL)
        iterms = re.findall(reg, html)
        # print iterms[0][0]
    except Exception as e:
        print e
        continue

    video_url = iterms[0]
    try:
        video = requests.get(video_url)
    except Exception as e:
        print e
        continue

    title = course_name + '.mp4'

    filename = os.path.join(dirpath, title)
    with open(filename, "wb") as f:
        f.write(video.content)

    time.sleep(1)

print u"全部视频信息下载完毕！尽情阅览！(^_^)"

exit()

