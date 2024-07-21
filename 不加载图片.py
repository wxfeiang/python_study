
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 创建Chrome浏览器选项对象
chrome_options = Options()

# 设置页面不加载图片,这样可以加快页面的渲染，减少爬虫的等待时间，提升爬取效率
# 固定配置如下：

# 使用headless无界面浏览器模式
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# 设置禁止加载图片的选项
prefs = {'profile.managed_default_content_settings.images': 2}
chrome_options.add_experimental_option("prefs", prefs)

# 启动Chrome浏览器并加载网页
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.taobao.com")

print( driver.title)

# 进行其他操作...

# 关闭浏览器
time.sleep(5)
# driver.quit()
# 这样就可以在打开网页时不加载图片了