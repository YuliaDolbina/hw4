from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


browser = webdriver.Chrome(
service = ChromeService(ChromeDriverManager().install()))

browser.get("http://uitestingplayground.com/textinput")

element = browser.find_element(By.CSS_SELECTOR, "#newButtonName")

element.send_keys("SkyPro")

button = browser.find_element(By.CSS_SELECTOR, "#updatingButton")

button.click()

print(button)