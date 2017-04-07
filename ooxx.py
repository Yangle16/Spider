#-*- coding:utf-8 -*-
import urllib,requests,urllib2
import re,os,sys

def downImg(imgUrl, dirpath, imgName):
    filename = os.path.join(dirpath, imgName)
    try:
        res = requests.get(imgUrl)
    except Exception as e:
        print("抛出异常：", imgUrl)
        print(e)
        return False
    with open(filename, "wb") as f:
        f.write(res.content)
    return True


def mkDir(dirName):
    dirpath = os.path.join(sys.path[0], dirName)
    if not os.path.exists(dirpath):
        os.mkdir(dirpath)
    return dirpath

dirpath = mkDir("imgxxoo")

m = 0

for i in range(1,501):
    a = str(i)
    print "正在获取并下载" + a + '页图片，请等待！'

    img_url = "http://jandan.net/ooxx" + '/page-' + a + '#comments'
    # print img_url
    try:
        sub_web = urllib.urlopen(img_url).read()
    except  Exception as e:
        print "获取连接失败，跳过"
        continue

    # 匹配内容 'src="(.*?)"'
    re_imgc = re.findall('<img src=\"(.*?)\"',sub_web)
    # print re_imgc
    b = 'http:'

    for x in re_imgc:
        img = b + x
        print img
        m += 1
        downImg(img, dirpath, str(m) + ".jpg")

print "美图全部下载完毕！请备好手纸(^_^)"
exit()