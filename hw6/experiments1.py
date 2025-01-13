from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(
service = ChromeService(ChromeDriverManager().install()))

browser.get("https://ya.ru/")
sleep(15)
element = browser.find_element(By.CSS_SELECTOR, "#text")
element.clear()
sleep(5)
element.send_keys("test")

element.send_keys(Keys.RETURN)
sleep(5)
#url = browser.current_url 
#print(url)

browser.quit()