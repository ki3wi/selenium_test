#coding=utf-8

from DataDrivenFrameWork.util.ObjectMap import *
from DataDrivenFrameWork.util.ParseConfigurationFile import ParseConfigFile

class HomePage(object):

    def __init__(self,driver):
        self.driver = driver
        self.parseCF = ParseConfigFile()
        self.homeOptions = self.parseCF.getOptionValue("126mail_homePage","homePage.addressbook")
        print self.homeOptions

    def addressLink(self):
        try:
            #从定位表达式配置文件中读取定位通讯录按钮的方式和表达式
            locateType,locatorExpression = self.homeOptions.split(">")
            elementObj = getElement(self.driver,locateType,locatorExpression)
            return elementObj
        except Exception ,e:
            raise e




if  __name__ == '__main__':
    from DataDrivenFrameWork.appModules.LoginAction import  LoginAction
    from selenium import webdriver
    import time
    #启动chrome浏览器
    driver = webdriver.Chrome(executable_path='c:\\chromedriver')
    #访问126邮箱
    driver.get('http://mail.126.com')
    #driver.maximize_window()
    time.sleep(5)
    LoginAction.login(driver,'','')
    time.sleep(5)
    homeObj = HomePage(driver)
    print homeObj
    homeObj.addressLink().click()
    driver.quit()

