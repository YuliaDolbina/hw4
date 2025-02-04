from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.color import Color
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


from EmptyPage import EmptyPage


def test_color():
    browser = Chrome(service=ChromeService(ChromeDriverManager().install()))
    empty_page = EmptyPage(browser)
    empty_page.find_element_by()
    empty_page.fill_in_the_gaps()
    empty_page.submit()
    empty_page.getting_ids()

    green_color = "#0f5132"
    red_color = "#842029"

    assert Color.from_string(zip_code.value_of_css_property("color")).hex == red_color
    assert (
        Color.from_string(first_name.value_of_css_property("color")).hex
        == Color.from_string(first_name.value_of_css_property("color")).hex
        == Color.from_string(last_name.value_of_css_property("color")).hex
        == Color.from_string(address.value_of_css_property("color")).hex
        == Color.from_string(city.value_of_css_property("color")).hex
        == Color.from_string(country.value_of_css_property("color")).hex
        == Color.from_string(email.value_of_css_property("color")).hex
        == Color.from_string(phone.value_of_css_property("color")).hex
        == Color.from_string(job.value_of_css_property("color")).hex
        == Color.from_string(company.value_of_css_property("color")).hex
        == green_color
    )

