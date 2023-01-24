from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element('xpath', '//*[@id="cookie"]')

items = driver.find_element(
    'xpath', '//*[@id="store"]').find_elements(By.TAG_NAME, 'div')
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
five_min = time.time() + 60*5  # 5minutes

while True:
    cookie.click()

    # Every 5 seconds:
    if time.time() > timeout:

        # Get all upgrade <b> tags
        all_prices = driver.find_element(
            'xpath', '//*[@id="store"]').find_elements(By.TAG_NAME, 'b')
        item_prices = []

        # Convert <b> text into an integer price.
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        # Create dictionary of store items and prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        # Get current cookie count
        money_element = driver.find_element(By.ID, "money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        # Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        # Purchase the most expensive affordable upgrade
        if len(affordable_upgrades) != 0:
            highest_price_affordable_upgrade = max(affordable_upgrades)
            print(highest_price_affordable_upgrade)

            to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

            driver.find_element(By.ID, to_purchase_id).click()
        else:
            print("not enough resources")

        # Add another 5 seconds until the next check
        timeout = time.time() + 5
