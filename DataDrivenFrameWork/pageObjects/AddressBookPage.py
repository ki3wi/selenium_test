# coding=UTF-8
from DataDrivenFrameWork.util.ObjectMap import *
from DataDrivenFrameWork.util.ParseConfigurationFile import ParseConfigFile

class AddressBookPage(object):

    def __init__(self,driver):
        self.driver = driver
        self.parseCF = ParseConfigFile()
        self.addContactsOptions = self.parseCF.getItemSection('126mail_addContactsPage')
        print self.addContactsOptions



    def createContactPersonButton(self):
        #获取新建联系人按钮
        try:
            #从定位表达式配置文件中获取定位新建联系人按钮的定位方式和表达式
            locateType,locatorExpression = self.addContactsOptions\
                ['addContactsPage.creatContactsBtn'.lower()].split('>')
            #获取新建联系人按钮页面元素，用返回给调用者
            elemetObj = getElement(self.driver,locateType,locatorExpression)
            return elemetObj
        except Exception ,e:
            raise e

    def contactPersonName(self):
        #获取新建联系人界面中的姓名输入框
        try:
            locateType,locatorExpression = self.addContactsOptions\
            ['addContactsPage.contactPersonName'.lower()].split('>')
            #获取姓名输入框页面元素，并返回给调用者
            elementObj = getElement(self.driver,locateType,locatorExpression)
            return elementObj
        except Exception,e:
            raise e


    def contactPersonEmail(self):
        try:
            locateType,locatorExpression = self.addContactsOptions\
            ['addContactsPage.contactPersonEmail'.lower()].split('>')
            elementObj = getElement(self.driver,locateType,locatorExpression)
            return elementObj
        except Exception,e:
            raise e

    def startContacts(self):
        try:
            locateType,locatorExpression = self.addContactsOptions\
            ['addContactsPage.startContacts'.lower()].split('>')
            elementObj = getElement(self.driver,locateType,locatorExpression)
            return elementObj
        except Exception,e:
            raise e

    def contactPersonMobile(self):
        try:
            locateType,locatorExpression = self.addContactsOptions\
            ['addContactsPage.contactPersonMobile'.lower()].split('>')
            elementObj = getElement(self.driver,locateType,locatorExpression)
            return elementObj
        except Exception,e:
            raise e


    def contactPersonComment(self):
        try:
            locateType,locatorExpression = self.addContactsOptions\
            ['addContactsPage.contactPersonComment'.lower()].split('>')
            elementObj = getElement(self.driver,locateType,locatorExpression)
            return elementObj
        except Exception,e:
            raise e


    def savecontacePerson(self):
        try:
            locateType,locatorExpression = self.addContactsOptions\
            ['addContactsPage.savecontacePerson'.lower()].split('>')
            elementObj = getElement(self.driver,locateType,locatorExpression)
            return elementObj
        except Exception,e:
            raise e






