# -*- coding: utf-8 -*-

from selenium import webdriver
from KeyWordsFrameWork.config.VarConfig import ieDriverFilePath
from KeyWordsFrameWork.config.VarConfig import chromeDriverFilePath
from KeyWordsFrameWork.config.VarConfig import firefoxDriverFilePath
from KeyWordsFrameWork.util.ObjectMap import getElement
from KeyWordsFrameWork.util.ClipboardUtil import Clipboard
from KeyWordsFrameWork.util.KeyBoardUtil import KeyBoardKeys
from KeyWordsFrameWork.util.DirAndTime import *
from KeyWordsFrameWork.util.WaitUtil import WaitUtil
from selenium.webdriver.chrome.options import Options
import time

#定义全局driver变量
driver = None
#全局的等待类实例对象
waitUtil = None


def open_browser(browserName,* args):
    #打开浏览器
    global driver
    try:
        if browserName.lower() == "ie":
            driver = webdriver.Ie(executable_path = ieDriverFilePath)
        elif browserName.lower() == "chrome":
            #创建chrome浏览器的一个options实例对象
            chrome_options = Options()
            #添加屏蔽-- ignore-certificate-error提示信息的设置参数项
            chrome_options.add_experimental_option("excludeSwitchs",["ignore-certificate-errors"])
            driver = webdriver.Chrome(executable_path = chromeDriverFilePath,chrome_options = chrome_options)
        else:
            driver = webdriver.Firefox(executable_path = firefoxDriverFilePath)
        #driver对象创建成功后，创建等待类的实例对象
        waitUtil = WaitUtil(driver)
    except Exception,e:
        raise e

def visit_url(url,* args):
    #访问某个网址
    global driver
    try:
        driver.get(url)
    except Exception,e:
        raise e


def close_browser(* args):
    #关闭浏览器
    global driver
    try:
        driver.quit()
    except Exception,e:
        raise e

def sleep(sleepSeconds,* args):
    #强制等待
    try:
        time.sleep(int(sleepSeconds))
    except Exception,e:
        raise e

def clear(locationType,locatorExpression,* args):
    #清除输入框默认内容
    global driver
    try:
        getElement(driver,locationType,locatorExpression).clear()
    except Exception,e:
        raise e

def input_string(locationType,locatorExpression,inputContent):
    #在页面输入框中输入数据
    global driver
    try:
        getElement(driver,locationType,locatorExpression).send_keys(inputContent)
    except Exception,e:
        raise e


def click(locationType,locatorExpression,* args):
    #单击页面元素
    global driver
    try:
        getElement(driver,locationType,locatorExpression).click()
    except Exception,e:
        raise e

def assert_string_in_pagesource(assertString,* args):
    #断言页面源代码是否存在某关键字或关键字符串
    global driver
    try:
        assert assertString in driver.page_source, u"%s not found in page source!" %assertString
    except AssertionError,e:
        raise AssertionError(e)
    except Exception,e:
        raise e

def assert_title(titileStr,* args):
    #断言页面标题是否存在给定关键字字符串
    global driver
    try:
        assert titileStr in driver.title, u"%s not found in title!" %titileStr
    except AssertionError,e:
        raise AssertionError(e)
    except Exception,e:
        raise e


def getPageTitle(* args):
    #获取页面标题
    global driver
    try:
        return driver.title
    except Exception,e:
        raise e

def getPageSource(* args):
    #获取页面源码
    global driver
    try:
        return driver.page_source
    except Exception,e:
        raise e

def switch_to_frame(locationType,locatorExpression,* args):
    #切换进入frame
    global driver
    try:
        driver.switch_to.frame(getElement(driver,locationType,locatorExpression))
    except Exception,e:
        print "frame error"
        raise e

def switch_to_default_content(* args):
    #切出frame
    global driver
    try:
        driver.switch_to.default_content()
    except Exception,e:
        raise e

def paste_string(pasteString,* args):
    #模拟ctrl+v操作
    try:
        Clipboard.setText(paste_string)
        #等待2秒，防止代码执行的太快，而未成功粘贴内容
        time.sleep(2)
        KeyBoardKeys.twoKeys("ctrl","v")
    except Exception,e:
        raise e

def press_tab_key(* args):
    #模拟Tab键
    try:
        KeyBoardKeys.oneKey("tab")
    except Exception,e:
        raise e

def press_enter_key(* args):
    #模拟enter键
    try:
        KeyBoardKeys.oneKey("enter")
    except Exception,e:
        raise e


def maximize_browser():
    #窗口最大化
    global driver
    try:
        driver.maximize_window()
    except Exception,e:
        raise e

def capture_screen(* args):
    #截取屏幕图片
    global driver
    currTime = getCurrentTime()
    picNameAndPath = str(creatCurrentDateDir()) + "\\" + str(currTime) + ".png"
    try:
        driver.get_seceenshot_as_file(picNameAndPath.replace("\\",r"\\"))
    except Exception,e:
        raise e
    else:
        return picNameAndPath

def waitPresentOfElementLocated(locationType,locatorExpression,* args):
    '''
    显示等待页面元素出现在DOM中，但并不一定可见，存在则返回该页面元素对象
    :param locationType:
    :param locatorExpression:
    :param args:
    :return:
    '''
    global waitUtil
    try:
        waitUtil.presenceOfElementLocated(locationType,locatorExpression)
    except Exception,e:
        raise e

def waitFrameToBeAvailableAndSwitchToIt(locationType,locatorExpression,* args):
    '''检查frame是否讯在，存在则切换进frame控件中'''
    global waitUtil
    try:
        waitUtil.frameToBeAvailableAndSwitchToIt(locationType,locatorExpression)
    except Exception,e:
        raise e

def waitVisibilityOfElementLocated(locationType,locatorExpression,* args):
    '''
    显示等待页面元素出现在DOM中，并且可见，存在则返回该页面元素对象
    :param locationType:
    :param locatorExpression:
    :param args:
    :return:
    '''
    global waitUtil
    try:
        waitUtil.visibilityOfElementLocated(locationType,locatorExpression)
    except Exception,e:
        raise e


































