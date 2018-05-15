# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WaitUtil(object):

    def __init__(self,driver):
        self.locationTypeDict = {"xpath": By.XPATH,
                                 "id": By.ID,
                                 "name": By.NAME,
                                 "class_name": By.CLASS_NAME,
                                 "tag_name": By.TAG_NAME,
                                 "link_text": By.LINK_TEXT,
                                 "partial_link_text": By.PARTIAL_LINK_TEXT
                                 }
        self.driver = driver
        self.wait = WebDriverWait(self,driver,30)

    def frame_available_and_swith_to_it(self,locationType,locatorExpression):
        '''
        检查frame是否存在，存在则切换进frame控件中
        :param locationType:
        :param locatorExpression:
        :return:
        '''
        try:
            self.wait.until(EC.frame_to_be_available_and_switch_to_it
                            ((self.locationTypeDict[locationType.lower()], locatorExpression)))
        except Exception,e:
            raise e

    def visibility_element_located(self,locationType,locatorExpression):
        '''显式等待页面元素的出现 '''
        try:
            element = self.wait.until(EC.visibility_of_element_located
                                      ((self.locationTypeDict[locationType.lower()], locatorExpression)))
            return element
        except Exception,e:
            raise e

if __name__ == '__main__':
    from selenium import webdriver
    import time
    driver = webdriver.Chrome(executable_path="c:\\chromedriver")
    driver.get('http://mail.163.com')
    waitUtil = WaitUtil(driver)
    waitUtil.frame_available_and_swith_to_it("id", "x-URS-iframe")
    e = waitUtil.visibility_element_located("xpath", "//input[@name='email']")
    e.send_keys('success')
    time.sleep(6)
    driver.quit()



