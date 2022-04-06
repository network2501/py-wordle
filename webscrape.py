import imp
import logging
from time import sleep
from typing import final
from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

logging.basicConfig(level=logging.DEBUG)

options = Options()
# options.headless = True
options.add_argument("--disable-extensions")
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get("https://www.nytimes.com/games/wordle/index.html")
driver.implicitly_wait(20)
print(driver.title)
elements = driver.find_element_by_css_selector("game-app")
print(f"Thing:: {elements}")
