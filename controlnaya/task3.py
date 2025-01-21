from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

browser.get("https://www.saucedemo.com/")

input_username = "#user-name"
input_password = "#password"

search_input = browser.find_element(By.CSS_SELECTOR, input_username)
sleep(1)
search_input.send_keys("standard_user")
sleep(1)

search_input = browser.find_element(By.CSS_SELECTOR, input_password)
sleep(1)
search_input.send_keys("secret_sauce")
sleep(1)

button = "#login-button"
search_button = browser.find_element(By.CSS_SELECTOR, button).click()
sleep(5)

add_to_cart1 = browser.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()

sleep(2)
add_to_cart2 = browser.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()

sleep(2)
add_to_cart3 = browser.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

sleep(2)
cart = browser.find_element(By.CSS_SELECTOR, "#shopping_cart_container > a").click()

sleep(2)

checkout = browser.find_element(By.CSS_SELECTOR, "#checkout").click()

sleep(3)

name = browser.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Юлия")

last_name = browser.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Долбина")

code = browser.find_element(By.CSS_SELECTOR, "#postal-code").send_keys(111222)

sleep(5)

button_continue = browser.find_element(By.CSS_SELECTOR, "#continue").click()

sleep(3)

total = browser.find_element(By.CSS_SELECTOR, "#checkout_summary_container > div > div.summary_info > div.summary_total_label")

print(total.text)

quit()



