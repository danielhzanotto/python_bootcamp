from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

navegador = webdriver.Firefox()

navegador.get("https://www.amazon.com.br")
navegador.find_element("xpath",
                       '//*[@id="twotabsearchtextbox"]').send_keys(f"kindle 11ª geração")
navegador.find_element("xpath", '//*[@id="nav-search-submit-button"]').click()

name = navegador.find_element(
    'xpath', '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div[3]/div[1]/h2/a/span').text
price = navegador.find_element(
    'xpath', '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div[3]/div[3]/div/a[1]/span/span[2]/span[2]').text

print(name)
print(price)

navegador.quit()
