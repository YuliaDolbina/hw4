from selenium.webdriver import Chrome
from selenium.webdriver.support.color import Color
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import allure
from EmptyPage import EmptyPage

@allure.title("Проверить становится ли красным незаполненное поле")
def test_color():
    browser = Chrome(service=ChromeService(ChromeDriverManager().install()))

    empty_page = EmptyPage(browser)
    empty_page.fill_in_the_gaps()
    empty_page.submit()
    empty_page.getting_elements()

    green_color = "#0f5132"
    red_color = "#842029"

    with allure.step("Проверка цвета поля"):
        assert Color.from_string(empty_page.zip_code.value_of_css_property("color")).hex == red_color
        assert (
        Color.from_string(empty_page.first_name.value_of_css_property("color")).hex
        == Color.from_string(empty_page.last_name.value_of_css_property("color")).hex
        == Color.from_string(empty_page.address.value_of_css_property("color")).hex
        == Color.from_string(empty_page.city.value_of_css_property("color")).hex
        == Color.from_string(empty_page.country.value_of_css_property("color")).hex
        == Color.from_string(empty_page.email.value_of_css_property("color")).hex
        == Color.from_string(empty_page.phone.value_of_css_property("color")).hex
        == Color.from_string(empty_page.job.value_of_css_property("color")).hex
        == Color.from_string(empty_page.company.value_of_css_property("color")).hex
        == green_color
    )
