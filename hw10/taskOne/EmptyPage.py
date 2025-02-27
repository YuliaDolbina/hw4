import allure
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains



class EmptyPage:
    first_name: WebElement
    last_name: WebElement
    address: WebElement
    zip_code: WebElement
    city: WebElement
    country: WebElement
    email: WebElement
    phone: WebElement
    job: WebElement
    company: WebElement

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

        self._first_name_id = "first-name"
        self._last_name_id = "last-name"
        self._address_id = "address"
        self._zip_id = "zip-code"
        self._city_id = "city"
        self._country_id = "country"
        self._email_id = "e-mail"
        self._phone_id = "phone"
        self._job_id = "job-position"
        self._company_id = "company"


    @allure.step("Найти элемент")
    def find_element_by(self, by: By, path: str) -> WebElement:
        return self._driver.find_element(by, path)

    @allure.step("Заполнить поля данными")
    def fill_in_the_gaps(self):
        self.find_element_by(By.NAME, self._first_name_id).send_keys("Иван")
        self.find_element_by(By.NAME, self._last_name_id).send_keys("Петров")
        self.find_element_by(By.NAME, self._address_id).send_keys("Ленина, 55-3")
        self.find_element_by(By.NAME, self._zip_id).send_keys("")
        self.find_element_by(By.NAME, self._city_id).send_keys("Москва")
        self.find_element_by(By.NAME, self._country_id).send_keys("Россия")
        self.find_element_by(By.NAME, self._email_id).send_keys("test@skypro.com")
        self.find_element_by(By.NAME, self._phone_id).send_keys("+7985899998787")
        self.find_element_by(By.NAME, self._job_id).send_keys("QA")
        self.find_element_by(By.NAME, self._company_id).send_keys("SkyPro")

    @allure.step("Нажать на кнопку Submit")
    def submit(self):
        button_path = "body > main > div > form > div:nth-child(5) > div > button"
        button = self._driver.find_element(By.CSS_SELECTOR, button_path)
        ActionChains(self._driver).move_to_element(button).perform()
        button.click()

    @allure.step("Собрать информацию из полей")
    def getting_elements(self):
        self.first_name = self.find_element_by(By.ID, self._first_name_id)
        self.last_name = self.find_element_by(By.ID, self._last_name_id)
        self.address = self.find_element_by(By.ID, self._address_id)
        self.zip_code = self.find_element_by(By.ID, self._zip_id)
        self.city = self.find_element_by(By.ID, self._city_id)
        self.country = self.find_element_by(By.ID, self._country_id)
        self.email = self.find_element_by(By.ID, self._email_id)
        self.phone = self.find_element_by(By.ID, self._phone_id)
        self.job = self.find_element_by(By.ID, self._job_id)
        self.company = self.find_element_by(By.ID, self._company_id)
