import requests
import os

savepath = "/Users/wangpeng/project/Python/test1/hximg"
# 设定本地存储地址
if not os.path.exists(savepath):
    pass
if not os.path.exists(savepath):
    os.mkdir(savepath)


# 链接分析
def creat_request(page):
    url = "https://www.kuaishou.com/profile/3xizsn5vfwfmwsa"
    # if page == 1:
    #     url = "https://www.kuaishou.com/profile/3xizsn5vfwfmwsa"
    # else:
    #     url = "https://sc.chinaz.com/tupian/index_" + str(page) + ".html"

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.3"
    }
    response = requests.get(url, headers=headers)

    return response


from lxml import etree


def get_content(response):
    html = etree.HTML(str(response.text).encode("utf-8"))
    result = html.xpath("//div[@class='item']/img/@src")

    print(result)


# 开始资源下载
def down_load(response):
    html = etree.HTML(str(response.text).encode("utf-8"))
    print(html)

    fh = open("./hh.html", "wb")  # 将文件写入到当前目录中
    fh.write(str(response.text).encode("utf-8"))
    fh.close()

    # resultSrc = html.xpath("//div[@class='item']/img/@data-original")

    # for src in resultSrc:
    #     # print("https:" + src)
    #     url = "https:" + src
    #     res = requests.get(url)

    #     img_name = src.split("/").pop()

    #     with open(savepath + "/" + img_name, "wb") as f:
    #         f.write(res.content)
    #     print("下载完成：", img_name)


# 初始化入口
if __name__ == "__main__":
    start_page = int(input("请输入开始页："))
    end_page = int(input("请输入结束页："))
    for page in range(start_page, end_page + 1):
        # 请求对象
        response = creat_request(page)
        # 请求到的源码

        down_load(response)
