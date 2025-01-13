from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(
service = ChromeService(ChromeDriverManager().install()))


browser.get("https://labirint.ru/")

#browser.maximize_window()

#sleep(4)

#browser.minimize_window()

#sleep(4)

#browser.fullscreen_window()

#sleep(4)

