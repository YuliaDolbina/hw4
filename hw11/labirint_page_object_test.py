from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.CartPage import CartPage
from pages.MainPage import MainPage
from pages.ResultPage import ResultPage


def test_cart_counter():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    main_page = MainPage(browser)
    main_page.set_cookie_policy()
    main_page.search("Python")

    result_page = ResultPage(browser)
    to_be = result_page.add_books()

    cart_page = CartPage(browser)
    cart_page.go_to_cart()
    as_is = cart_page.get_counter()

    assert int(as_is.replace(" товара", "")) == to_be

#def test_empty_search():
    #browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    #main_page = MainPage(browser)
    #main_page.set_cookie_policy()
    #main_page.search("")

