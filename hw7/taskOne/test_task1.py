from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


from EmptyPage import EmptyPage
from FilledPage import FilledPage

def test_color():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    empty_page = EmptyPage(browser)
    empty_page.fill_in_the_gaps()
    empty_page.submit()

    filled_page = FilledPage(browser)
    filled_page.getting_ids()

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

