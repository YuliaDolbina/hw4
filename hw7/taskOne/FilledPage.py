from selenium.webdriver.common.by import By


class FilledPage:
    def __init__(self, browser):
        self._driver = browser


    def getting_ids():
        
        first_name = find_element_by(browser, By.ID, first_name_id)
        last_name = find_element_by(browser, By.ID, last_name_id)
        address = find_element_by(browser, By.ID, address_id)
        zip_code = find_element_by(browser, By.ID, zip_id)
        city = find_element_by(browser, By.ID, city_id)
        country = find_element_by(browser, By.ID, country_id)
        email = find_element_by(browser, By.ID, email_id)
        phone = find_element_by(browser, By.ID, phone_id)
        job = find_element_by(browser, By.ID, job_id)
        company = find_element_by(browser, By.ID, company_id)    
