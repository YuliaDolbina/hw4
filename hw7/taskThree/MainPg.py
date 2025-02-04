from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class MainPg:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")


    def find_element_by(self, by: By, path: str) -> WebElement:
        return self._driver.find_element(by, path)
    
    def authorize(self):
        input_username = "#user-name"
        input_password = "#password"

        search_input = self._driver.find_element(By.CSS_SELECTOR, input_username)
        search_input.send_keys("standard_user")

        search_input = self._driver.find_element(By.CSS_SELECTOR, input_password)

        search_input.send_keys("secret_sauce")

        button = "#login-button"
        search_button = self._driver.find_element(By.CSS_SELECTOR, button)
        ActionChains(self._driver).move_to_element(search_button).perform()
        search_button.click()
        
    def add_to_cart(self):
        thing1 = self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
        ActionChains(self._driver).move_to_element(thing1).perform()
        thing1.click()

        thing2 = self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")
        ActionChains(self._driver).move_to_element(thing2).perform()
        thing2.click()

        thing3 = self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie")
        ActionChains(self._driver).move_to_element(thing3).perform()
        thing3.click()  

      



    
