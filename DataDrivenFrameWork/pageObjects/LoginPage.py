# coding:utf-8
from DataDrivenFrameWork.util.ObjectMap import *
from DataDrivenFrameWork.util.ParseConfigurationFile import  ParseConfigFile

class LoginPage(object):
    def __init__(self,driver):
        self.driver = driver
        self.parseCF = ParseConfigFile()
        self.loginOptions = self.parseCF.getItemSection("126mail_login")
        print self.loginOptions

    def switchToFrame(self):
        try:
            #从定位表达式配置文件中读取frame的定位表达式
            loactorExpression = self.loginOptions["loginPage.frame".lower()].split(">")[1]
            self.driver.switch_to.frame(loactorExpression)
        except Exception ,e:
            raise e


    def switchToDefaultFrame(self):
            try:
                self.driver.switch_to.default_content()
            except Exception ,e:
                raise e


    def userNameObj(self):
        try:
            #从定位表达式配置文件中读取定位用户名输入框的定位方式和表达式
            locateType,locatorExpression = self.loginOptions["loginPage.username".lower()].split(">")
            #获取登录页面的用户名输入框页面对象，并返回给调用者
            elementObj = getElement(self.driver,locateType,locatorExpression)
            return elementObj

        except Exception ,e:
            raise e


    def passwordObj(self):
        try:
            locateType,locatorExpression = self.loginOptions["loginPage.password".lower()].split(">")
            #获取登录页面的密码输入框页面的对象，用返回给调用者
            elementObj = getElement(self.driver,locateType,locatorExpression)
            return elementObj

        except Exception ,e:
            raise e


    def loginButton(self):
        try:
            locateType,locatorExpression = self.loginOptions["loginPage.loginbutton".lower()].split(">")
            #获取登录页面的登录按页面对象，用返回给调用者
            elementObj = getElement(self.driver,locateType,locatorExpression)
            return elementObj
        except Exception,e:
            raise e

if __name__ == '__main__':
    #测试代码
    from selenium import webdriver
    driver = webdriver.Chrome(executable_path = 'c:\\chromedriver')
    driver.get("http://mail.126.com")
    import time
    time.sleep(5)
    login = LoginPage(driver)
    login.switchToFrame()
    login.userNameObj().send_keys("")
    login.passwordObj().send_keys('')
    login.loginButton().click()
    time.sleep(5)
    login.switchToDefaultFrame()
    time.sleep(5)
    assert u"未读邮件" in driver.page_source
    driver.quit()






