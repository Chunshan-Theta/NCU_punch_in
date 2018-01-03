#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime

ChromeDriveDir ="/usr/lib/chromium-browser/chromedriver"
WaitLoadTime = 2

driver = webdriver.Chrome(ChromeDriveDir)

#    go to page
driver.get("http://human.is.ncu.edu.tw/HumanSys/login")
time.sleep(WaitLoadTime)
elem = driver.find_element_by_id("userid_input")
elem.send_keys('***********')
elem = driver.find_element_by_name("j_password")
elem.send_keys('*************')
elem.send_keys(Keys.RETURN)
driver.get("http://human.is.ncu.edu.tw/HumanSys/student/stdSignIn")
