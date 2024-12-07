from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

button = "#content > div > button"

search_input = driver.find_element(By.CSS_SELECTOR, button)
sleep(1)
for _ in range(5):
    search_input.click()
    sleep(1)

list_of_buttons = "added-manually"
search_list = driver.find_elements(By.CLASS_NAME, list_of_buttons)
print("Количество кнопок:", len(search_list))

sleep(5)
driver.close()


