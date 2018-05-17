# -*-coding: utf-8 -*-

import os

ieDriverFilePath = "c:\\IEDriverServer"
chromeDriverFilePath = "c:\\chromedriver"
firefoxDriverFilePath = "c:\\geckdriver"

#获取当前文件所在目录的父目录的绝对路径
#C:\Users\ki3wi\shan\selenium_test\KeyWordsFrameWork
parentDirPath  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#print parentDirPath
#C:\Users\ki3wi\shan\selenium_test\KeyWordsFrameWork\config
#parentDirPath2  = os.path.dirname(os.path.abspath(__file__))
#print parentDirPath2
#C:\Users\ki3wi\shan\selenium_test\KeyWordsFrameWork\config\VarConfig.py
#parentDirPath3  = os.path.abspath(__file__)
#print parentDirPath3
screenPictureDir = parentDirPath + "\\exceptionpictures\\"
print screenPictureDir


