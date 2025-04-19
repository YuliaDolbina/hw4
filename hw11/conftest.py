import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.webdriver import WebDriver

@pytest.fixture
def driver():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    return browser


