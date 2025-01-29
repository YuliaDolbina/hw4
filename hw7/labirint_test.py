from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

cookie = {"name": "cookie_policy",
          "value": "1"}

def test_cart_counter():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.get("https://www.labirint.ru")
    browser.implicitly_wait(4)
    browser.maximize_window()
    browser.add_cookie(cookie)

    browser.find_element(By.CSS_SELECTOR, "#search-field").send_keys("python")
    browser.find_element(By.CSS_SELECTOR, "#searchform > div.b-search-e-input-wrapper > button > span.b-header-b-search-e-btntxt").click()

    buy_buttons = browser.find_element(By.CSS_SELECTOR, "a._btn.btn-tocart.buy-link")

    print(len(buy_buttons))

    sleep(5)

    browser.quit()


        