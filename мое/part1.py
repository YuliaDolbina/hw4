from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager as FirefoxManager
from selenium.webdriver.common.by import By


options = webdriver.FirefoxOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Firefox(service=FirefoxService(FirefoxManager().install()), options=options)

driver.get("")


enter = "body"
search_enter = driver.find_element(By.CSS_SELECTOR, enter)


input_username = "#username"
input_password = "#password"

search_input = driver.find_element(By.CSS_SELECTOR, input_username)
sleep(1)
search_input.send_keys("tomsmith")
sleep(1)

search_input = driver.find_element(By.CSS_SELECTOR, input_password)
sleep(1)
search_input.send_keys("SuperSecretPassword!")
sleep(1)

button = "#login > button > i"
search_button = driver.find_element(By.CSS_SELECTOR, button)
sleep(1)
search_button.click()

sleep(5)
driver.close()