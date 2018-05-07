# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 09:12:05 2018

@author: tuant
"""

#def fblogin():
#    from selenium import webdriver
#    from getpass import getpass
#    usr = input("Input your user name or email or phone: \n")
#    pwd = getpass("Enter your pass: \n")
#    
#    browser = webdriver.Chrome()
#    browser.get("https://www.facebook.com")
#    
#    username_box = browser.find_element_by_id("email")
#    username_box.send_keys(usr)
#    
#    password_box = browser.find_element_by_id("pass")
#    password_box.send_keys(pwd)
#    
#    login_btn = browser.find_element_by_id("loginbutton")
#    login_btn.submit()
#    
#fblogin()

import time
from selenium import webdriver

driver = webdriver.Chrome('/path/to/chromedriver')  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/xhtml');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()