from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class EmptyPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    def find_element_by(self, by: By, path: str) -> WebElement:
        return self._driver.find_element(by, path)
    
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

        self.find_element_by(By.NAME, first_name_id).send_keys("Иван")
        self.find_element_by(By.NAME, last_name_id).send_keys("Петров")
        self.find_element_by(By.NAME, address_id).send_keys("Ленина, 55-3")
        self.find_element_by(By.NAME, zip_id).send_keys("")
        self.find_element_by(By.NAME, city_id).send_keys("Москва")
        self.find_element_by(By.NAME, country_id).send_keys("Россия")
        self.find_element_by(By.NAME, email_id).send_keys("test@skypro.com")
        self.find_element_by(By.NAME, phone_id).send_keys("+7985899998787")
        self.find_element_by(By.NAME, job_id).send_keys("QA")
        self.find_element_by(By.NAME, company_id).send_keys("SkyPro")


    def submit(self):
        button_path = "body > main > div > form > div:nth-child(5) > div > button"
        button = self._driver.find_element(By.CSS_SELECTOR, button_path)
        ActionChains(self._driver).move_to_element(button).perform()
        button.click()



    def getting_ids(self):

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
                
        first_name = self.find_element_by(By.ID, first_name_id)
        last_name = self.find_element_by(By.ID, last_name_id)
        address = self.find_element_by(By.ID, address_id)
        zip_code = self.find_element_by(By.ID, zip_id)
        city = self.find_element_by(By.ID, city_id)
        country = self.find_element_by(By.ID, country_id)
        email = self.find_element_by(By.ID, email_id)
        phone = self.find_element_by(By.ID, phone_id)
        job = self.find_element_by(By.ID, job_id)
        company = self.find_element_by(By.ID, company_id)

        return first_name, last_name,address, zip_code, city, country, email, phone, job, company




