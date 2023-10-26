# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 22:54:50 2023

@author: c.samanja09
"""

from bs4 import BeautifulSoup

import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get('https://therealdeal.com/new-york/')

driver.maximize_window()
time.sleep(5)
driver.execute_script("window.scrollBy(0,600)", "")
tags=driver.find_elements(By.TAG_NAME,'article')
time.sleep(5)
tags[0].click()
time.sleep(5)
print(driver.current_url)

url1=driver.current_url

driver.back()