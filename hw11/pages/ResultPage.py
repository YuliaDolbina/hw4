from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class ResultPage:
    def __init__(self, browser):
        self._driver = browser

    def add_books(self):
        buy_buttons = self._driver.find_elements(By.CSS_SELECTOR, "._btn.btn-tocart.buy-link")
        counter = 0
        for btn in buy_buttons:
            goods_id = btn.get_attribute("data-idtov")
            ActionChains(self._driver).move_to_element(btn).perform()
            btn.click()

            like_btn = self._driver.find_element(By.CSS_SELECTOR, f"[data-id_book='{goods_id}']")
            like_btn.click()

            counter += 1
            sleep(1)

        return counter
