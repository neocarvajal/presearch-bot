#!/usr/bin/env python -*- coding: utf-8 -*-

"""
Python script for automated  firefox web browser search on presearch.org.

Presearch is an open, decentralized search engine that rewards community members 
with Presearch Tokens for their usage, contribution to, and promotion of the platform.

All this project is based on Selenium. You can install it from here:
https://selenium-python.readthedocs.io/installation.html

web: https://www.presearch.org/signup?rid=1257758
"""

import time
import os
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

HOME_DIRECTORY = os.environ.get('HOME')

options = webdriver.FirefoxOptions()

options.add_argument("--width=800");

options.add_argument("--height=640");

profile = webdriver.FirefoxProfile(HOME_DIRECTORY + "/.mozilla/firefox/fao18bjc.default")

options.binary_location = "/usr/bin/firefox"

browser = webdriver.Firefox(firefox_profile=profile,firefox_options=options)

def busqueda(palabra):

	#time.sleep(10)

	print("Navegando a presearch... \n")

	browser.get("https://www.presearch.org/?utm_source=extcr")
	
	try:
	    element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "search")))
	finally:
		print("Buscando... " + palabra + "\n")
		element.send_keys(palabra, Keys.ENTER)
		
	try:
	    element = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='r']/a[1]")))
	finally:
		results = []

	links = browser.find_elements_by_xpath("//div[@class='r']/a")
	
	for link in links:			
		results.append(link.get_attribute("href"))
		print("Enlace encontrado: " + link.get_attribute("href") + "\n")
		
	link = random.choice(results)
		
	print("Navegando a " + link + "\n")
	
	link = browser.find_element_by_xpath("//a[starts-with(@href,'"+ link + "')]").click()

	time.sleep(10)		 

archivo = open("search.txt", "r")

for palabra in archivo.readlines():
	busqueda(palabra)

browser.close()

__author__ = "Erick Carvajal"
__copyright__ = "Copyright 2019, presearch.py"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "@neocarvajal"
__email__ = "neocarvajal@gmail.com"
__status__ = "Production"