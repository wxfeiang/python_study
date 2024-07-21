
import time
# 导入selenium包
from selenium import webdriver
from selenium.webdriver.common.by import By



# 启动并打开指定页面
browser = webdriver.Chrome()
browser.get("https://www.taobao.com")

# 确保加载完成
time.sleep(5)

# 通过css定位输入框,输入内容selenium
browser.find_element(By.CSS_SELECTOR, '#session_email_or_mobile_number').send_keys('18309469751')
browser.find_element(By.CSS_SELECTOR,'#session_password').send_keys('wp258258')
browser.find_element(By.CSS_SELECTOR,'#sign-in-form-submit-btn').click()
browser.find_element(By.XPATH, '//input[@id="kw"]').send_keys('selenium')

# 停留五秒后关闭浏览器
time.sleep(5)
browser.quit()


