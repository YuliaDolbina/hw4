import allure
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from Summa import Sum

@allure.title("Проверка сложения")
@allure.description("Проверка калькулятора, сложение")
@allure.feature("READ")
@allure.severity("Major")
def test_summa():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    sum = Sum(browser)
    result = sum.summa()
    with allure.step("Проверить результат"):
        assert result == "15"

