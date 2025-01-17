from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


browser = webdriver.Chrome(
service = ChromeService(ChromeDriverManager().install()))

browser.get("http://uitestingplayground.com/ajax")

sleep(15)
button = "#ajaxButton"

element = browser.find_element(By.CSS_SELECTOR, button).click()

text = "#content > p"

green_box = browser.find_element(By.CSS_SELECTOR, text)
sleep(5)

print(green_box)

sleep(5)