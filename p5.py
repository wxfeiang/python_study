import requests

url = "https://www.baidu.com/"

print("请求的URL是：", url)
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.3"
}
response = requests.get(url, headers=headers)


fh = open("./b.html", "wb")  # 将文件写入到当前目录中
fh.write(str(response.text).encode("utf-8"))
fh.close()
