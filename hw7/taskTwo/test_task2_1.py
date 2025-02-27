from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from Summa import Sum

def test_summa():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    sum = Sum(browser)
    result = sum.summa()

    assert result == "15"

