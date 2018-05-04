#coding: utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path="c:\\chromedriver")
driver.implicitly_wait(10)
driver.get("http://mail.126.com/")


time.sleep(5)

driver.switch_to_frame("x-URS-iframe")
userName = driver.find_element_by_xpath('//input[@name="email"]')
userName.clear()
userName.send_keys("")
pwd = driver.find_element_by_xpath('//input[@name="password"]')
pwd.clear()
pwd.send_keys("")
pwd.send_keys(Keys.RETURN)

time.sleep(10)
driver.find_element_by_xpath("//li[@title='通讯录']").click()
time.sleep(2)
driver.find_element_by_xpath("//span[text()='新建联系人']").click()
time.sleep(2)
driver.find_element_by_xpath("//input[@id='input_N']").send_keys(u"邢")
driver.find_element_by_xpath("//*[@id='iaddress_MAIL_wrap']//input").send_keys("xing@sina.com")
driver.find_element_by_xpath("//span[text()='设为星标联系人']").click()
##
driver.find_element_by_xpath("//*[@id='iaddress_TEL_wrap']//dd//input").send_keys("1581109999")

driver.find_element_by_xpath("//textarea[@id='input_DETAIL']").send_keys("boyfriend")
driver.find_element_by_xpath("//span[text()='确 定']").click()
time.sleep(2)
driver.quit()







