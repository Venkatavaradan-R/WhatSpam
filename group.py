from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Replace below path with the absolute path
# to chromedriver in your computer

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('headless')
driver = webdriver.Chrome('/home/venkat/github/WhatSpam/chromedriver_linux64/chromedriver', chrome_options=chrome_options)


driver.get("https://web.whatsapp.com/")
# # wait = WebDriverWait(driver, 600)
# time.sleep(25)

# # Replace 'Friend's Name' with the name of your friend
# # or the name of a group
# target = '"Chandradeep Choudhury"'

# # Replace the below string with your own message
# string = "PySpam Activated"

# x_arg = '//span[contains(@title,' + target + ')]'
# group_title = wait.until(EC.presence_of_element_located((
#     By.XPATH, x_arg)))
# group_title.click()
# inp_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'
# input_box = wait.until(EC.presence_of_element_located((
#     By.XPATH, inp_xpath)))
# for i in range(100):
#     input_box.send_keys(string + Keys.ENTER)
#     time.sleep(1)
