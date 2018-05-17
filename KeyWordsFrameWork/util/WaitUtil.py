# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# class WaitUtil(object):
#
#     def __init__(self,driver):
#         self.locationTypeDict = {"xpath": By.XPATH,"id": By.ID,"name": By.NAME,"class_name": By.CLASS_NAME,"tag_name": By.TAG_NAME,"link_text": By.LINK_TEXT,"partial_link_text": By.PARTIAL_LINK_TEXT}
#         self.driver = driver
#         self.wait = WebDriverWait(self,driver,30)
#
#     def frame_available_and_swith_to_it(self,locationType,locatorExpression):
#         '''
#         检查frame是否存在，存在则切换进frame控件中
#         '''
#         try:
#             self.wait.until(EC.frame_to_be_available_and_switch_to_it((self.locationTypeDict[locationType.lower()], locatorExpression)))
#
#         except Exception,e:
#             raise e
#
#     def visibility_element_located(self,locationType,locatorExpression):
#         '''显式等待页面元素的出现 '''
#         try:
#             element = self.wait.until(EC.visibility_of_element_located((self.locationTypeDict[locationType.lower()], locatorExpression)))
#             return element
#         except Exception,e:
#             raise e
#
# if __name__ == '__main__':
#     from selenium import webdriver
#     from selenium.webdriver.support.ui import WebDriverWait
#     from selenium.webdriver.support import expected_conditions as EC
#     import time
#     driver = webdriver.Chrome(executable_path="c:\\chromedriver")
#     driver.get('http://mail.163.com')
#     #waitU = WaitUtil(driver)
#     waitU = WebDriverWait(driver,30)
#     #WebDriverWait(driver,30).until(EC.frame_to_be_available_and_switch_to_it((By.ID,"x-URS-iframe")))
#     waitU.until(EC.frame_to_be_available_and_switch_to_it((By.ID,"x-URS-iframe")))
#     #e = WebDriverWait(driver,30).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='email']")))
#     #waitUtil.frame_available_and_swith_to_it("id","x-URS-iframe")
#     e = waitU.until(EC.visibility_of_element_located((By.XPATH,"//input[@name='email']")))
#     e.send_keys('success')
#     time.sleep(6)
#     driver.quit()


class WaitUtil(object):

    def __init__(self,driver):
        self.locationTypeDict = {"xpath": By.XPATH,"id": By.ID,"name": By.NAME,"class_name": By.CLASS_NAME,"tag_name": By.TAG_NAME,"link_text": By.LINK_TEXT,"partial_link_text": By.PARTIAL_LINK_TEXT}
        self.driver = driver
        self.wait = WebDriverWait(self,driver,30)

    def presenceOfElementLocated(self,locatorMethod,locatorExpression,*args):
        '''
        显示等待页面元素出现在DOM中，但并不一定可见，存在则返回该页面元素对象
        '''
        try:
            if self.locationTypeDict.has_key(locatorMethod.lower()):
                self.wait.until(EC.presence_of_element_located((self.locationTypeDict[locatorMethod.lower()],locatorExpression)))
            else:
                raise TypeError(u"未找到定位方式，请确认定位方法是否写正确")
        except Exception,e:
            raise e


    def frameToBeAvailableAndSwitchToIt(self,locationType,locatorExpression,*args):
        """
        检查frame是否存在，存在则切换进frame控件中
        """
        try:
            self.wait.until(EC.frame_to_be_available_and_switch_to_it((self.locationTypeDict[locationType.lower()], locatorExpression)))
        except Exception,e:
            #抛出异常给上层掉用者
            raise e


    def visibilityOfElementLocated(self,locationType,locatorExpression,*args):
        '''显式等待页面元素的出现在DOM中，并且可见，存在则返回该页面元素对象 '''
        try:
            self.wait.until(EC.visibility_of_element_located((self.locationTypeDict[locationType.lower()], locatorExpression)))
        except Exception,e:
            raise e

if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome(executable_path="c:\\chromedriver")
    driver.get('http://mail.163.com')
    waitU = WaitUtil(driver)
    waitU.frameToBeAvailableAndSwitchToIt("id","x-URS-iframe")
    waitU.visibilityOfElementLocated("xpath", "//input[@name='email']")
    waitU.presenceOfElementLocated("xpath", "//input[@name='email']")
    driver.quit()
