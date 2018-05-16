# -*- coding: utf-8 -*-

from KeyWordsFrameWork.util.ObjectMap import *
from KeyWordsFrameWork.util.KeyBoardUtil import KeyBoardKeys
from KeyWordsFrameWork.util.ClipboardUtil import Clipboard
from KeyWordsFrameWork.util.WaitUtil import WaitUtil
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def TestSendMailWithAttachment():
    #创建Chrome浏览器实例
    driver = webdriver.Chrome(executable_path='c:\\chromedriver')
    print u"启动浏览器成功"
    print u"访问163邮箱登录页"
    driver.get("http://mail.163.com")
    time.sleep(5)
    assert u"163网易免费邮--中文邮箱第一品牌" in driver.title,u"title断言失败"
    print u'访问163邮箱页面成功!'
    wait = WaitUtil(driver)
    wait.frame_available_and_swith_to_it("id","x-URS-iframe")
    print u"输入登录用户名"
    username = getElement(driver,"xpath","//input[@name='email']")
    username.send_keys("shanqm")
    print u"输入登录密码"
    pwd = getElement(driver,"xpath","//input[@name='password']")
    pwd.send_keys("xxx")
    pwd.send_keys(Keys.ENTER)
    print u'用户登陆..'
    time.sleep(5)
    assert u'网易邮箱' in driver.title
    print u'登陆成功！'


    element = wait.visibility_element_located("xpath","//span[text()='写 信']")
    element.click()
    print u"准备写信..."
    receiver = getElement(driver,"xpath","//div[contains(@id,'_mail_emailinput')]/input")
    receiver.send_keys('shan_5210@126.com')
    subject = getElement(driver,"xpath","//div[@aria-label='邮件主题输入框，请输入邮件主题']/input")
    subject.send_keys(u"新邮件")
    #设置剪贴板内容
    Clipboard.setText(u"‪C:\\Users\\ki3wi\\Desktop\\要记住的.txt")
    #获得剪贴板内容
    Clipboard.getText()
    attachment = getElement(driver,"xpath","//div[contains(@title,'装饰器笔记')]")
    # 单击上传附件链接
    attachment.click()
    time.sleep(3)
    #在上传附件Windows弹窗中粘贴剪贴板中的内容
    KeyBoardKeys.twoKeys("ctrl","v")
    #模拟回车键，以便加载要上传的附件
    KeyBoardKeys.oneKey("enter")
    #切换进邮件正文
    wait.frame_available_and_swith_to_it("xpath","//iframe[@tabindex=1]")
    body = getElement(driver,"xpath","/html/body")
    #输入邮件正文
    body.send_keys(u'这是自动发送的邮件')
    #切出邮件正文的frame框
    driver.switch_to.default_content()
    print u'写信完成'
    getElement(driver,"xpath","//header//span[text()='发送']").click()
    print u'开始发送..'
    time.sleep(3)
    assert u'发送成功' in driver.page_source
    print u'邮件发送成功！'
    driver.quit()


if __name__ == '__main__':
    TestSendMailWithAttachment()