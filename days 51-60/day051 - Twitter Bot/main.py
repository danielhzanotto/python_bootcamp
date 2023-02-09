from selenium import webdriver
from selenium.webdriver.common.by import By
import time

DOWNLOAD_BASE = 100
UPLOAD_BASE = 100
TWITTER_MAIL = ''
TWITTER_PASS = ''
TWITTER_USER = ''

driver = webdriver.Firefox()

driver.get('https://www.speedtest.net/')

driver.find_element(
    'xpath', '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]').click()

timer = time.time() + 50
while timer >= time.time():
    continue

download = driver.find_element(
    'xpath', '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
upload = driver.find_element(
    'xpath', '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text


print(download)
print(upload)

if float(download) < DOWNLOAD_BASE or float(upload) < UPLOAD_BASE:
    print("hora de reclamar!!!")

driver.get('https://www.twitter.com/login')

time.sleep(2)

driver.find_element(
    'xpath', '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input').send_keys(TWITTER_MAIL)
driver.find_element(
    'xpath', '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span').click()

time.sleep(2)

try:
    driver.find_element(
        'xpath', '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys(TWITTER_PASS)
    driver.find_element(
        'xpath', '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span').click()
except:
    driver.find_element(
        'xpath', '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input').send_keys(TWITTER_USER)
    driver.find_element(
        'xpath', '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/span/span').click()
    time.sleep(2)
    driver.find_element(
        'xpath', '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys(TWITTER_PASS)
    driver.find_element(
        'xpath', '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span').click()

time.sleep(5)

driver.find_element(
    'xpath', '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div').click()

time.sleep(1)


driver.find_element(
    'xpath', '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div').send_keys('teste')
