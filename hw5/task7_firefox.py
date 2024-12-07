from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager as FirefoxManager
from selenium.webdriver.common.by import By


options = webdriver.FirefoxOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Firefox(service=FirefoxService(FirefoxManager().install()), options=options)


driver.get("https://the-internet.herokuapp.com/inputs")

input = "#content > div > div > div > input[type=number]"

search_input = driver.find_element(By.CSS_SELECTOR, input)
sleep(1)
search_input.send_keys("1000")
sleep(1)
search_input.clear()
sleep(1)
search_input.send_keys("999")

sleep(5)
driver.close()