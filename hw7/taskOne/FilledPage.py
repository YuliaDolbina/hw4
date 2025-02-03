from selenium.webdriver.common.by import By


class FilledPage:
    def __init__(self, browser):
        self._driver = browser


    def getting_ids(self):
                
        first_name = find_element_by(self._driver, By.ID, first_name_id)
        last_name = find_element_by(self._driver, By.ID, last_name_id)
        address = find_element_by(self._driver, By.ID, address_id)
        zip_code = find_element_by(self._driver, By.ID, zip_id)
        city = find_element_by(self._driver, By.ID, city_id)
        country = find_element_by(self._driver, By.ID, country_id)
        email = find_element_by(self._driver, By.ID, email_id)
        phone = find_element_by(self._driver, By.ID, phone_id)
        job = find_element_by(self._driver, By.ID, job_id)
        company = find_element_by(self._driver, By.ID, company_id)    
