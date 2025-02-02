from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class Sum:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def summa(self):
        num1 = self._driver.find_element(By.CSS_SELECTOR, "#delay")
        num1.clear()
        num1.send_keys(45)

        num2 = self._driver.find_element(By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(1)")
        ActionChains(self._driver).move_to_element(num2).perform()
        num2.click()
        num3 = self._driver.find_element(By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(4)")
        ActionChains(self._driver).move_to_element(num3).perform()
        num3.click()
        num4 = self._driver.find_element(By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(2)")
        ActionChains(self._driver).move_to_element(num4).perform()
        num4.click()
        num5 = self._driver.find_element(By.CSS_SELECTOR, "#calculator > div.keys > span.btn.btn-outline-warning")
        ActionChains(self._driver).move_to_element(num5).perform()
        num5.click()

        text = "#calculator > div.top > div"
    
        num = self._driver.find_element(By.CSS_SELECTOR, text)
        print(num.text)


