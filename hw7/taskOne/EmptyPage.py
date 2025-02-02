from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class EmptyPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")


    def fill_in_the_gaps(self):

        first_name_id = "first-name"
        last_name_id = "last-name"
        address_id = "address"
        zip_id = "zip-code"
        city_id = "city"
        country_id = "country"
        email_id = "e-mail"
        phone_id = "phone"
        job_id = "job-position"
        company_id = "company"

        find_element_by(self._driver, By.NAME, first_name_id).send_keys("Иван")
        find_element_by(self._driver, By.NAME, last_name_id).send_keys("Петров")
        find_element_by(self._driver, By.NAME, address_id).send_keys("Ленина, 55-3")
        find_element_by(self._driver, By.NAME, zip_id).send_keys("")
        find_element_by(self._driver, By.NAME, city_id).send_keys("Москва")
        find_element_by(self._driver, By.NAME, country_id).send_keys("Россия")
        find_element_by(self._driver, By.NAME, email_id).send_keys("test@skypro.com")
        find_element_by(self._driver, By.NAME, phone_id).send_keys("+7985899998787")
        find_element_by(self._driver, By.NAME, job_id).send_keys("QA")
        find_element_by(self._driver, By.NAME, company_id).send_keys("SkyPro")


    def submit(self):
       
       button_path = "body > main > div > form > div:nth-child(5) > div > button"
       button = self._driver.find_element(By.CSS_SELECTOR, button_path)
       ActionChains(self._driver).move_to_element(button).perform()
       button.click()