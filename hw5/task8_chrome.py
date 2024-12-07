from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)


driver.get("https://the-internet.herokuapp.com/login")

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
