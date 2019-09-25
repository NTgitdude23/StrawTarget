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
options.headless = True
options.add_argument("--incognito")
options.add_argument("--log-level=3")

delay = 10 # seconds

target = input("What poll would you like to target: ")


option = input("Does this poll contain a captcha:(yes/no): ")

vote = input("Which box would you like to check(name(Needs to be all lowercase and make sure you have dashes for spaces.)): ")

total_votes = int(input("How many votes would you like?: "))

opit = "field-options-"+vote

def randomline(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)


def strawpoll():
	try:
		PROXY = randomline("proxies.txt")
		options.add_argument('--proxy-server=%s' % PROXY)
		driver = webdriver.Chrome("chromedriver.exe", options=options)
		driver.get(target)
		driver.find_element_by_id(opit).click()
		time.sleep(1)
		sumbit_button = driver.find_element(By.XPATH, '//button[text()="Vote"]')
		sumbit_button.click()
		wait = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'vote-count')))
		print("Vote added")
		driver.quit()
	except:
		driver.quit()

def strawpoll2():
	try:
		PROXY = randomline("HTTPS_ProxyList2.txt")
		options.add_argument('--proxy-server=%s' % PROXY)
		driver = webdriver.Chrome("chromedriver.exe", options=options)
		driver.get(target)
		driver.find_element_by_id(opit).click()
		time.sleep(1)
		elem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'g-recaptcha')))
		elem.click()
		sumbit_button = driver.find_element(By.XPATH, '//button[text()="Vote"]')
		sumbit_button.click()
		try:
			wait = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'vote-count')))
			print("Vote added, not blocked by captcha.")
			driver.quit()
		except:
			pass
			print("Blocked by Captcha") 
			driver.quit()
	except:
		driver.quit()



if option == "no":
	while total_votes > 0:
		try:
			strawpoll()
			total_votes -= 1
		except:
			pass
			print("There was an issue in the attempt, retrying...")
			total_votes += 1

elif "yes":
	while total_votes > 0:
		try:
			strawpoll2()
			total_votes -= 1
		except:
			pass
			print("Captcha blocked attempt, retrying...")
			total_votes += 1
else:
	print("This is not a valid option.")

