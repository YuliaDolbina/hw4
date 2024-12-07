from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)


driver.get("http://the-internet.herokuapp.com/entry_ad")

button = "//*[@class='modal-footer']"

search_modal = driver.find_element(By.XPATH, button)
sleep(1)
driver.execute_script('arguments[0].click()', search_modal)

sleep(5)
driver.close()
