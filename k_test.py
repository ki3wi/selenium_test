# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium .webdriver.common.keys import Keys
from selenium.webdriver.common.by import By




print u'启动浏览器...'
driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
#driver = webdriver.Firefox(executable_path='D:\\firefox\\geckodriver.exe')
#driver.maximize_window()
print u'启动浏览器成功...'
print u'访问163邮箱...'
driver.get('http://mail.163.com')
driver.implicitly_wait(15)
assert u"163网易免费邮--中文邮箱第一品牌" in driver.title,u"title断言失败"
print u'访问163邮箱页面成功!'
wait = WebDriverWait(driver,30)
wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID,"x-URS-iframe")))
#time.sleep(5)
#driver.switch_to_frame("x-URS-iframe")
username = driver.find_element_by_xpath('//input[@name="email"]')
username.send_keys("shanqm")
pwd = driver.find_element_by_xpath("//input[@name='password']")
pwd.send_keys("xxx")
pwd.send_keys(Keys.RETURN)
print u'用户登陆..'
time.sleep(5)
assert u'网易邮箱' in driver.title
print u'登陆成功！'

print u'准备写信..'
element = wait.until(EC.visibility_of_element_located((By.XPATH,"//span[text()='写 信']")))
element.click()
driver.find_element_by_xpath("//div[contains(@id,'_mail_emailinput')]/input").send_keys('shan_5210@126.com')
driver.find_element_by_xpath("//div[@aria-label='邮件主题输入框，请输入邮件主题']/input").send_keys(u"新邮件")
driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@tabindex=1]"))
editBox = driver.find_element_by_xpath("/html/body")
editBox.send_keys(u'这是自动发送的邮件')
driver.switch_to.default_content()
print u'写信完成'
driver.find_element_by_xpath("//header//span[text()='发送']").click()
print u'开始发送..'
time.sleep(3)
assert u'发送成功' in driver.page_source
print u'邮件发送成功！'
driver.quit()

