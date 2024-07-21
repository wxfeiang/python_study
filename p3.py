import urllib.request
import urllib.parse

url = "http://www.baidu.com/s?wd="
keyword = "Python 教程"
key_code = urllib.request.quote(keyword)  # 对请求进行编码
url_all = url + key_code
print(url_all)
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.3"
}

# 头部信息
request = urllib.request.Request(url=url_all, headers=headers)

# 发送请求
reponse = urllib.request.urlopen(request)


content = reponse.read().decode("utf-8")


fh = open("./urllib_test_runoob_search.html", "wb")  # 将文件写入到当前目录中
fh.write(content)
fh.close()
