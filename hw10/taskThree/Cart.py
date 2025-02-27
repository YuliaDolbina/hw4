import allure
from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class Cart:
    def __init__(self, browser):
        self._driver = browser

    @allure.step("Перейти в корзину")
    def go_to_cart(self):
        cart = self._driver.find_element(By.CSS_SELECTOR, "#shopping_cart_container > a")
        ActionChains(self._driver).move_to_element(cart).perform()
        cart.click()

    @allure.step("Подтвердить заказ в корзине")
    def checkout(self):
        check_out = self._driver.find_element(By.CSS_SELECTOR, "#checkout")
        ActionChains(self._driver).move_to_element(check_out).perform()
        check_out.click()

    @allure.step("Заполнить поля данными")
    def filling_the_application(self):
        name = self._driver.find_element(By.CSS_SELECTOR, "#first-name")
        name.send_keys("Юлия")

        last_name = self._driver.find_element(By.CSS_SELECTOR, "#last-name")
        last_name.send_keys("Долбина")

        code = self._driver.find_element(By.CSS_SELECTOR, "#postal-code")
        code.send_keys(111222)

        button_continue = self._driver.find_element(By.CSS_SELECTOR, "#continue")
        ActionChains(self._driver).move_to_element(button_continue).perform()
        button_continue.click()

    @allure.step("Получить итоговую сумму заказа")
    def total(self):
        total = self._driver.find_element(By.CSS_SELECTOR, "#checkout_summary_container > div > div.summary_info > div.summary_total_label")
        return total.text



