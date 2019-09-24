import time
import unittest
from selenium import *
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import random
import string
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


banner = ('''
 +--^----------,--------,-----,--------^-,
 | |||||||||   `StrawTarget'  |          O
 `+---------------------------^----------|
   `\_,---------,---------,--------------'
     / XXXXXX /'|       /'
    / XXXXXX /  `\    /'
   / XXXXXX /`-------'
  / XXXXXX /
 / XXXXXX /
(________(        
 `------'

''')
print(banner)

options = Options()
options.headless = False
options.add_argument("--incognito")
options.add_argument("--log-level=3")

delay = 10 # seconds

target = input("What poll would you like to target: ")


option = input("Does this poll contain a captcha:(yes/no): ")

vote = input("Which box would you like to check(name(Needs to be all lowercase and make sure you have dashes for spaces.)): ")

total_votes = input("How many votes would you like?: ")

opit = "field-options-"+vote

def randomline(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)


def strawpoll():
	PROXY = randomline("HTTPS_ProxyList2.txt")
	options.add_argument('--proxy-server=%s' % PROXY)
	driver = webdriver.Chrome("chromedriver.exe", options=options)
	driver.get(target)
	#myelem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'field-options-' + vote))).click()
	#driver.find_element_by_xpath(".//*[@id="'field-options-option-1'"]").click()
	driver.find_element_by_id(opit).click()
	time.sleep(1)
	driver.find_element_by_id('<button type="button" class="embed"><span>Share</span></button>').click()
	option_button = chrome.find_elements_by_xpath('//*[@type="submit"]')[0]
	option_button.click()
	sumbit_button = chrome.find_elements_by_xpath('//footer/button')[0]
	sumbit_button.click()

def strawpoll2():
	PROXY = randomline("HTTPS_ProxyList2.txt")
	options.add_argument('--proxy-server=%s' % PROXY)
	driver = webdriver.Chrome("chromedriver.exe", options=options)
	driver.get(target)
	elem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'g-recaptcha')))
	captcha = ("Target has re-captcha: Would you like to brute force it?:(yes/no)")

	'''
	if captcha == yes:
		try:
			driver.find_element_by_id('g-recaptcha').click()

'''




if option == "no":
	strawpoll()

elif "yes":
	strawpoll2()

else:
	print("This is not a valid option.")






'''
	elem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'g-recaptcha')))
	captcha = ("Target has re-captcha: Would you like to brute force it?:(yes/no)")
	if captcha == yes:
		elem.click()
	else:
		print("Ok Exiting StrawTarget...")
		#except:
			driver.get()
	#except:
		print("ProxyError")
'''
