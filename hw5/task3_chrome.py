from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

button = "div.example"

search_input = driver.find_element(By.CSS_SELECTOR, button) 
search_input.send_keys(Keys.RETURN)

sleep(10)


