import allure
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from MainPg import MainPg
from Cart import Cart

@allure.title("Проверить стоимость товаров в корзине")
def test_number_of_goods():
    browser = Chrome(service=ChromeService(ChromeDriverManager().install()))

    main_page = MainPg(browser)
    main_page.authorize()
    main_page.add_to_cart()

    cart = Cart(browser)
    cart.go_to_cart()
    cart.checkout()
    cart.filling_the_application()
    price = cart.total()
    with allure.step("Проверка цены"):
        assert price == "Total: $58.29"



