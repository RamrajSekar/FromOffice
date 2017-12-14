'''
Created on 30-Jun-2017

@author: E002040
'''
user = "ramraj.sekar"
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Firefox()
browser.get("https://www.gmail.com")

#Get title
print(browser.title)
email = browser.find_element_by_xpath("//*[contains(@id,'identifier')]").send_keys(user)
btnext = browser.find_element_by_xpath("//*[contains(@id,'identifierNext')]").click()
time.sleep(20)
epwd = browser.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input").send_keys("test")
#time.sleep(5)
btnext = browser.find_element_by_xpath("//*[contains(@id,'passwordNext')]").click()
time.sleep(20)
print(browser.title)
#browser.close()

#===============================================================================
# import sys, webbrowser
# 
# ie = webbrowser.get(webbrowser.iexplore)
# ie.open('http://google.com')
#===============================================================================

