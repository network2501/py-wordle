import logging
from typing import final

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType


from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


logging.basicConfig(level=logging.DEBUG)

driver = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

# driver.get("https://www.nytimes.com/games/wordle/index.html")
# print(driver.title)

# element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, "game-app")))
# print(driver.title)
# elements = driver.find_element_by_css_selector("game-app")
# print(f"Thing:: {elements}")
