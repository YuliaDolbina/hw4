from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)


driver.get("http://uitestingplayground.com/classattr")

button = "//*[@class='btn class1 btn-primary btn-test']"

search_input = driver.find_element(By.XPATH, button)
sleep(1)

search_input.click()

sleep(5)
driver.close()
