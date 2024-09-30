from time import sleep 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.get("http://ya.ru")

driver.get("http://vk.com")
           
for x in range(1, 10):
    driver.back()
    driver.forward()


sleep(15)