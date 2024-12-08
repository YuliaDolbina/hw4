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

driver.get("http://the-internet.herokuapp.com/entry_ad")

button = "//*[@class='modal-footer']"

search_modal = driver.find_element(By.XPATH, button)
sleep(1)
driver.execute_script('arguments[0].click()', search_modal)

sleep(5)
driver.close()