from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

browser.get("http://uitestingplayground.com/ajax")

button = "#ajaxButton"

browser.find_element(By.CSS_SELECTOR, button).click()

text = "#content > p"
try:
    element = WebDriverWait(browser, 15).until(
        expected_conditions.presence_of_element_located((By.CSS_SELECTOR, text))
    )
except Exception:
    raise

green_box = browser.find_element(By.CSS_SELECTOR, text)

print(green_box.text)
