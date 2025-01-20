from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

browser.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

image_id = "award"
try:
    element = WebDriverWait(browser, 20).until(
        expected_conditions.presence_of_element_located((By.ID, image_id))
    )
except Exception:
    raise

image = browser.find_element(By.ID, image_id)

print(image.get_attribute("src"))
