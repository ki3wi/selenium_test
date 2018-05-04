#coding:utf-8
'''
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
import time

def testMailLogin():
    try:
        #启动浏览器
        driver = webdriver.Chrome(executable_path="chromedriver")
        driver.get("http://mail.126.com")
        driver.implicitly_wait(30)
        driver.maximize_window()
        loginPage = LoginPage(driver)
        loginPage.switchToFrame()
        loginPage.userNameObj().send_keys("")
        loginPage.userNameObj().send_keys("xx")
        loginPage.loginButton().click()
        time.sleep(3)
        loginPage.switchToDefaultFrame()
        assert u"未读邮件" in driver.page_source
    except Exception,e:
        raise e
    finally:
        driver.quit()

if __name__ == '__main__':
    testMailLogin()
    print u"登录126邮箱成功"
'''
#
# from selenium import webdriver
# from DataDrivenFrameWork.appModules.LoginAction import LoginAction
# import time
#
# def testMailLogin():
#     try:
#         driver = webdriver.Chrome(executable_path="c://chromedriver")
#         driver.get("http://mail.126.com")
#         time.sleep(5)
#         LoginAction.login(driver,username="",password="")
#         time.sleep(5)
#         driver.quit()
#
#     except Exception,e:
#         raise e
#
# if __name__ == '__main__':
#     testMailLogin()
#     print u"登陆成功"

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from DataDrivenFrameWork.util.ParseExcel import ParseExcel
# from DataDrivenFrameWork.config.VarConfig import *
# from DataDrivenFrameWork.appModules.LoginAction import LoginAction
# from DataDrivenFrameWork.appModules.AddContactPersonAction import AddContactPerson
# import traceback
# from time import sleep
#
# #设置此次测试环境编码为utf-8
# import sys
# reload(sys)
#
# #重建解析Excel对象
# excelObj = ParseExcel()
# #将Excel数据文件加载到内存
# dataFilePath = u'C:\\Users\\ki3wi\\PycharmProjects\\selenium_test\\DataDrivenFrameWork\\testData\\126邮箱联系人.xlsx'
# excelObj.loadWorkBook(dataFilePath)
#
# def LaunchBrowser():
#     #创建chrome浏览器的一个options实例对象
#     chrome_options = Options()
#     #向Options是实例中添加禁用扩展插件的设置参数项
#     chrome_options.add_argument("--disable-extensions")
#     #添加屏蔽 --ignore-certificate-errors提示信息的设置参数项
#     chrome_options.add_experimental_option("excludeSwithes",["ignore-certificate-errors"])
#     #添加浏览器最大化的参数设置参数项，已启动就是最大化
#     chrome_options.add_argument('--start-maxmized')
#     #启动带有自定义设置的chrome浏览器
#     driver = webdriver.Chrome(executable_path="c:\\chromeDriver",chrome_options = chrome_options)
#     #访问126邮箱
#     driver.get("http://mail.126.com")
#     sleep(3)
#     return driver
#
# def test126MailAddContacts():
#     try:
#         #根据Excel文件中sheet名称获取此sheet对象
#         userSheet = excelObj.getSheetByName(u'126账号')
#         #获取126账号sheet中是否执行行列
#         isExecuteUser = excelObj.getColumn(userSheet,account_isExecute)
#         #print  isExecuteUser
#         #获取126账号sheet中的数据表列
#         dataBookColumn = excelObj.getColumn(userSheet,account_dataBook)
#         #print dataBookColumn
#         print u'测试126邮箱添加联系人执行开始'
#         for idx,i in enumerate(isExecuteUser[1:]):
#             print idx ,i
#             #循环遍历126账号表中账号，为需要执行的账号添加联系人
#             if i.value == 'y':#表示执行
#                 #获取第i行的数据
#                 userRow = excelObj.getRow(userSheet,idx + 2)
#                 print userRow
#                 #获取第i行中的用户名
#                 username = userRow[account_username - 1].value
#                 #获取第i行中的密码
#                 password = str(userRow[account_password - 1].value)
#                 print username,password
#
#                 #创建浏览器实例对象
#                 driver = LaunchBrowser()
#                 #登录126邮箱
#                 LoginAction.login(driver,username,password)
#                 #等待3秒，让浏览器启动完成，以便正常的进行后续的操作
#                 sleep(3)
#                 #获取为第i行中用户添加的联系人数据表sheet名
#                 dataBookName = dataBookColumn[idx + 1].value
#                 #获取对应的数据表对象
#                 dataSheet = excelObj.getSheetByName(dataBookName)
#                 #获取联系人数据表中是否执行对象
#                 isExecuteData = excelObj.getColumn(dataSheet,contacts_isExecute)
#                 contacteNum = 0 #记录添加成功联系人个数
#                 isExecuteNum = 0 #记录需要执行联系人个数
#                 for id,data in enumerate(isExecuteData[1:]):
#                     #虚幻遍历是否执行添加新联系人列，
#                     #如果被设置为添加，则进行联系人添加操作
#                     if data.value == "y":
#                         #如果第id行的联系人被设置为执行，则isExecuteNum自增1
#                         isExecuteNum += 1
#                         #获取联系人表第id+2行对象
#                         rowContent = excelObj.getRow(dataSheet,id + 2)
#                         print rowContent
#                         #获取联系人姓名
#                         contactPersonName = rowContent[contacts_contactPersonName - 1].value
#                         #获取联系人邮箱
#                         contactPersonEmail = rowContent[contacts_contactPersonEmail - 1].value
#                         #获取是否设置为星标联系人
#                         isStart = rowContent[contacts_isStart - 1].value
#                         #获取联系人手机号
#                         contactPersonPhone = rowContent[contacts_contactPersonMobile - 1].value
#                         #获取联系人备注信息
#                         contactPersonComment = rowContent[contacts_contactPersonComment - 1].value
#                         #添加联系人成功后，断言关键字
#                         assertKeyWord = rowContent[contacts_assertKeyWords - 1].value
#                         print contactPersonName,contactPersonEmail,assertKeyWord
#                         print contactPersonPhone,contactPersonComment,isStart
#                         #执行新建联系人操作
#                         AddContactPerson.add(driver,contactPersonName,contactPersonEmail,isStart,contactPersonPhone,contactPersonComment)
#                         sleep(1)
#                         #在联系人工作表中写入添加联系人执行时间
#                         excelObj.writeCellCurrentTime(dataSheet,rowNo=id + 2,colsNo = contacts_runTime)
#                         try:
#                             #断言给定的关键字是否出现在页面中
#                             assert assertKeyWord in driver.page_source
#                         except AssertionError,e:
#                             #断言失败，在联系人工作表中写入添加联系人测试失败信息
#                             excelObj.writeCell(dataSheet,"faild",rowNo= id + 2,colsNo = contacts_testResult,style="red")
#                         else:
#                             #断言成功，写入添加联系人成功信息
#                             excelObj.writeCell(dataSheet,"pass",rowNo=id+2,colsNo=contacts_testResult,style='green')
#                             contacteNum +=1
#                         print "contactNum = %s,isExecuteNum = %s" %(contacteNum,isExecuteNum)
#                         if contacteNum == isExecuteNum:
#                             #如果成功添加的联系人数与需要添加的联系人数相等，
#                             #说明给第i个用户添加联系人测试用例执行成功，
#                             #在126账号工作表中写入成功信息，否则写入信息失败
#                             excelObj.writeCell(userSheet,"pass",rowNo= idx + 2,colsNo = account_testResult,style="green")
#                             print u"为用户%s添加%d个联系人，测试通过！" %(username,contacteNum)
#                         else:
#                             excelObj.writeCell(userSheet,"faild",rowNo=idx + 2,colsNo= account_testResult,style="red")
#                     else:
#                         print u"用户%s被设置为忽略执行！" %excelObj.getCellOfValue(userSheet,rowNo=idx+2,colsNo=account_username)
#                 driver.quit()
#     except Exception,e:
#         print u"数据驱动框架主程序发生异常，异常信息为："
#         #打印议程堆栈信息
#         print traceback.print_exc()
# if __name__ == '__main__':
#     test126MailAddContacts()


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from DataDrivenFrameWork.util.ParseExcel import ParseExcel
from DataDrivenFrameWork.config.VarConfig import *
from DataDrivenFrameWork.appModules.LoginAction import LoginAction
from DataDrivenFrameWork.appModules.AddContactPersonAction import AddContactPerson
import traceback
from time import sleep
from DataDrivenFrameWork.util.Log import *

#设置此次测试环境编码为utf-8
# import sys
# reload(sys)

#重建解析Excel对象
excelObj = ParseExcel()
#将Excel数据文件加载到内存
dataFilePath = u'C:\\Users\\ki3wi\\PycharmProjects\\selenium_test\\DataDrivenFrameWork\\testData\\126邮箱联系人.xlsx'
excelObj.loadWorkBook(dataFilePath)

def LaunchBrowser():
    #创建chrome浏览器的一个options实例对象
    chrome_options = Options()
    #向Options是实例中添加禁用扩展插件的设置参数项
    chrome_options.add_argument("--disable-extensions")
    #添加屏蔽 --ignore-certificate-errors提示信息的设置参数项
    chrome_options.add_experimental_option("excludeSwithes",["ignore-certificate-errors"])
    #添加浏览器最大化的参数设置参数项，已启动就是最大化
    chrome_options.add_argument('--start-maxmized')
    #启动带有自定义设置的chrome浏览器
    driver = webdriver.Chrome(executable_path="c:\\chromeDriver",chrome_options = chrome_options)
    #访问126邮箱
    driver.get("http://mail.126.com")
    sleep(3)
    return driver

def test126MailAddContacts():
    logging.info(u'126邮箱添加联系人数据驱动开始测试...')
    try:
        #根据Excel文件中sheet名称获取此sheet对象
        userSheet = excelObj.getSheetByName(u'126账号')
        #获取126账号sheet中是否执行行列
        isExecuteUser = excelObj.getColumn(userSheet,account_isExecute)
        #print  isExecuteUser
        #获取126账号sheet中的数据表列
        dataBookColumn = excelObj.getColumn(userSheet,account_dataBook)
        print dataBookColumn
        #print u'测试126邮箱添加联系人执行开始'
        for idx,i in enumerate(isExecuteUser[1:]):
            #循环遍历126账号表中账号，为需要执行的账号添加联系人
            if i.value == 'y':#表示执行
                #获取第i行的数据
                userRow = excelObj.getRow(userSheet,idx + 2)
                #print userRow
                #获取第i行中的用户名
                username = userRow[account_username - 1].value
                #获取第i行中的密码
                password = str(userRow[account_password - 1].value)
                print username,password

                #创建浏览器实例对象
                driver = LaunchBrowser()
                logging.info(u'启动浏览器，访问126邮箱主页')

                #登录126邮箱
                LoginAction.login(driver,username,password)
                #等待3秒，让浏览器启动完成，以便正常的进行后续的操作
                sleep(3)
                try:
                    #断言登录后跳转页面的标题是否包含“网易邮箱”
                    assert u'收 信' in driver.page_source
                    logging.info(u'用户%s登录后，断言页面关键字“收 信”成功' %username)
                except AssertionError,e:
                    logging.debug(u'用户%s登录后，断言页面关键字“收 信”失败' u'异常信息：%s'%(username,str(traceback.format_exc())))

                #获取为第i行中用户添加的联系人数据表sheet名
                dataBookName = dataBookColumn[idx + 1].value
                #获取对应的数据表对象
                dataSheet = excelObj.getSheetByName(dataBookName)
                #获取联系人数据表中是否执行对象
                isExecuteData = excelObj.getColumn(dataSheet,contacts_isExecute)
                contacteNum = 0 #记录添加成功联系人个数
                isExecuteNum = 0 #记录需要执行联系人个数
                for id,data in enumerate(isExecuteData[1:]):
                    #虚幻遍历是否执行添加新联系人列，
                    #如果被设置为添加，则进行联系人添加操作
                    rowContent = excelObj.getRow(dataSheet,id + 2)
                    contactPersonName = rowContent[contacts_contactPersonName - 1].value
                    if data.value == "y":
                        #如果第id行的联系人被设置为执行，则isExecuteNum自增1
                        isExecuteNum += 1
                        #获取联系人表第id+2行对象
                        #rowContent = excelObj.getRow(dataSheet,id + 2)
                        #print rowContent
                        #获取联系人姓名
                        #contactPersonName = rowContent[contacts_contactPersonName - 1].value
                        #获取联系人邮箱
                        contactPersonEmail = rowContent[contacts_contactPersonEmail - 1].value
                        #获取是否设置为星标联系人
                        isStart = rowContent[contacts_isStart - 1].value
                        #获取联系人手机号
                        contactPersonPhone = rowContent[contacts_contactPersonMobile - 1].value
                        #获取联系人备注信息
                        contactPersonComment = rowContent[contacts_contactPersonComment - 1].value
                        #添加联系人成功后，断言关键字
                        assertKeyWord = rowContent[contacts_assertKeyWords - 1].value
                        print contactPersonName,contactPersonEmail,assertKeyWord
                        print contactPersonPhone,contactPersonComment,isStart
                        #执行新建联系人操作
                        AddContactPerson.add(driver,contactPersonName,contactPersonEmail,isStart,contactPersonPhone,contactPersonComment)
                        sleep(1)
                        logging.info(u'添加联系人%s成功' %contactPersonName)
                        #在联系人工作表中写入添加联系人执行时间
                        excelObj.writeCellCurrentTime(dataSheet,rowNo=id + 2,colsNo = contacts_runTime)
                        try:
                            #断言给定的关键字是否出现在页面中
                            assert assertKeyWord in driver.page_source
                        except AssertionError,e:
                            #断言失败，在联系人工作表中写入添加联系人测试失败信息
                            excelObj.writeCell(dataSheet,"faild",rowNo= id + 2,colsNo = contacts_testResult,style="red")
                            logging.info(u'断言关键字%s失败' %assertKeyWord)
                        else:
                            #断言成功，写入添加联系人成功信息
                            excelObj.writeCell(dataSheet,"pass",rowNo=id+2,colsNo=contacts_testResult,style='green')
                            contacteNum +=1
                            logging.info(u'断言关键字%s成功'% assertKeyWord)
                        #print "contactNum = %s,isExecuteNum = %s" %(contacteNum,isExecuteNum)
                    else:
                        logging.info(u"联系人%s被忽略执行！" % contactPersonName)
                        if contacteNum == isExecuteNum:
                            #如果成功添加的联系人数与需要添加的联系人数相等，
                            #说明给第i个用户添加联系人测试用例执行成功，
                            #在126账号工作表中写入成功信息，否则写入信息失败
                            excelObj.writeCell(userSheet,"pass",rowNo= idx + 2,colsNo = account_testResult,style="green")
                            #print u"为用户%s添加%d个联系人，测试通过！" %(username,contacteNum)
                        else:
                            excelObj.writeCell(userSheet,"faild",rowNo=idx + 2,colsNo= account_testResult,style="red")
                            logging.info(u"为用户%s添加%d个联系人,%d个成功\n" %(username,isExecuteNum,contacteNum))
            else:
                #获取被忽略执行的用户名
                ignoreUserName = excelObj.getCellOfValue(userSheet,rowNo=idx + 2,colsNo=account_username)
                logging.info(u"用户%s被忽略执行！" % ignoreUserName)
    except Exception,e:
        logging.debug(u"数据驱动框架主程序发生异常，异常信息: %s" %str(traceback.format_exc()))
        driver.quit()

if __name__ == '__main__':
    test126MailAddContacts()


