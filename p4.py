from lxml import etree
html_str = '''
<div>
    <ul>
         <li class="item1"><a href="link1.html">Python</a></li>
         <li class="item2"><a href="link2.html">Java</a></li>
         <li class="site1"><a href="www.CSDN.net">CSDN</a>
         <li class="site2"><a href="www.baidu.com">百度</a></li>
         <li class="site3"><a href="www.jd.com">京东</a></li>
     </ul>
</div>
'''
html = etree.HTML(html_str)


# tostring()将标签元素转换为字符串输出，注意：result为字节类型
result = etree.tostring(html)
print(result.decode('utf-8'))



# parse_html= etree.HTML(html)

# 书写xpath表达式,提取文本最终使用text()
xpath_bds='//a/text()'
# 提取文本数据，以列表形式输出
r_list= html.xpath(xpath_bds)
# 打印数据列表
print(r_list)
