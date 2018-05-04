# -*- coding: utf-8 -*-
'''
实现定位页面元素
'''

from selenium.webdriver.support.ui import WebDriverWait

def getElement(driver,locationType,locatorExpression):
    try:
        element = WebDriverWait(driver,30).until(lambda x:x.find_element(by=locationType,value=locatorExpression))
        return element
    except Exception,e:
        raise e

def getElements(driver,locationType,locatorExpression):
    try:
        elements = WebDriverWait(driver,30).until(lambda x:x.find_elements(by=locationType,value=locatorExpression))
        return elements
    except Exception,e:
        raise e

if __name__ == '__main__':
    from selenium import webdriver
    import time
    driver = webdriver.Chrome(executable_path='c:\\chromedriver')
    driver.get('http://www.baidu.com')
    searchBox = getElement(driver,'id','kw')
    print searchBox.tag_name
    aList = getElements(driver,'tag name','a')
    print len(aList)
    a = lambda y:y.find_element(by='id',value='su')
    print a
    time.sleep(4)
    driver.quit()

