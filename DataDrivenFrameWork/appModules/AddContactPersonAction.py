# coding=UTF-8

from DataDrivenFrameWork.pageObjects.HomePage import HomePage
from DataDrivenFrameWork.pageObjects.AddressBookPage import AddressBookPage
import traceback
import time

class AddContactPerson(object):
    def __init__(self):
        print "add contact person"

    @staticmethod
    def add(driver,contactName,contactEmail,isStar,contactPersonPhone,contactComment):
        try:
            #创建主页实例对象
            hp = HomePage(driver)
            #单击通讯录链接
            hp.addressLink().click()
            time.sleep(3)
            #创建添加联系人页面实例对象
            apb = AddressBookPage(driver)
            apb.createContactPersonButton().click()
            if contactName:
                #非必填项
                apb.contactPersonName().send_keys(contactName)
            #必填项
            apb.contactPersonEmail().send_keys(contactEmail)
            if isStar ==u'是':
                #非必填项
                apb.startContacts().click()
            if contactPersonPhone:
                #非必填项
                apb.contactPersonMobile().send_keys(contactPersonPhone)
            if contactComment:
                apb.contactPersonComment().send_keys(contactComment)
            apb.savecontacePerson().click()
        except Exception,e:
            #打印堆栈异常信息
            print traceback.print_exc()

if __name__ == '__main__':
    from LoginAction import LoginAction
    from selenium import webdriver
    from DataDrivenFrameWork.pageObjects.HomePage import HomePage
    from DataDrivenFrameWork.pageObjects.AddressBookPage import AddressBookPage
    import time
    #启动chrome浏览器
    driver = webdriver.Chrome(executable_path='c:\\chromedriver')
    #访问126邮箱
    driver.get('http://mail.126.com')
    #driver.maximize_window()
    time.sleep(5)
    LoginAction.login(driver,'','')
    time.sleep(5)
    AddContactPerson().add(driver,u'周四','zhangsan@qq.com',u'是','15666633456',u'备注')
    time.sleep(6)
    assert u'周四' in driver.page_source
    driver.quit()

