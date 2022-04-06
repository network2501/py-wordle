# py-wordle

Getting an Information Theory fix by interacting with Worlde using Selenium.  

Shadowroot in geckdriver isn't available [link](https://github.com/SeleniumHQ/selenium/issues/10217). Moving to the chrome driver. 

## GeckoDriver

If Shadowroot wasn't an issue this is how I'd set things up. 

Use a drive manager to handle the browser if you're in a venv it'll help avoid needing to set environment variables for paths. 

```python
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager


options = Options()
options.add_argument("--disable-extensions")
# options.headless = True
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get("https://www.nytimes.com/games/wordle/index.html")
element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, "game-app")))
print(f"Thing:: {element}")
```
