from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, browser):
        self._driver = browser

    def go_to_cart(self):
        self._driver.get("https://www.labirint.ru/cart/")    

    def get_counter(self):
        txt = self._driver.find_element(By.CSS_SELECTOR, "#basket-default-prod-count2").text
        return txt    