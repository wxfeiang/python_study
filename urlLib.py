import urllib.request

url = 'http://www.baidu.com'

res = urllib.request.urlopen(url)

contet  = res.read().decode('utf-8')


fh = open("./urllib_test_post_runoob.html","wb")    # 将文件写入到当前目录中





