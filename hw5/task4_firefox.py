from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager as FirefoxManager
from selenium.webdriver.common.by import By


driver = webdriver.Firefox(service=FirefoxService(FirefoxManager().install()))


options = webdriver.FirefoxOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Firefox(service=FirefoxService(FirefoxManager().install()), options=options)


driver.get("http://uitestingplayground.com/dynamicid")

button = "//*[@class='btn btn-primary']"

search_input = driver.find_element(By.XPATH, button)
sleep(1)

search_input.click()

sleep(5)
driver.close()
