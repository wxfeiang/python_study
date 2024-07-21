import urllib.request

print("hello world")
url = 'http://www.baidu.com'
response = urllib.request.urlopen(url)

f = open("runoob_urllib_test.html", "wb")



content = response.read()  # 读取网页内容
f.write(content)
f.close()

encode_url = urllib.request.quote("https://www.runoob.com/")  # 编码
print(encode_url)

unencode_url = urllib.request.unquote(encode_url)    # 解码
print(unencode_url)



