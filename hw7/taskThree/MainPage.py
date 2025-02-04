from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class MainPage:
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


    def 
    
