from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

cookie = {"name": "cookie_policy",
          "value": "1"}

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def open_labirint ():
    browser.get("https://www.labirint.ru")
    browser.implicitly_wait(4)
    browser.maximize_window()
    browser.add_cookie(cookie)

def search(term):
    browser.find_element(By.CSS_SELECTOR, "#search-field").send_keys(term)
    browser.find_element(By.CSS_SELECTOR, "#searchform > div.b-search-e-input-wrapper > button > span.b-header-b-search-e-btntxt").click()

def add_books():
    buy_buttons = browser.find_elements(By.CSS_SELECTOR, "._btn.btn-tocart.buy-link")
    counter = 0
    for btn in buy_buttons:
        btn.click()
        counter += 1

    return counter 

def go_to_cart():
    browser.get("https://www.labirint.ru/cart/")

def get_cart_count():
    txt = browser.find_element(By.CSS_SELECTOR, "#basket-default-prod-count2").text
    return txt

def close_browser():
    browser.quit()

def test_cart_counter():

    open_labirint()

    search('python')

    added = add_books()

    go_to_cart()

    cart_count = get_cart_count()

    close_browser()

    assert added == int(cart_count.replace(" товара", ""))
    

    


        