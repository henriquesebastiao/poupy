from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from project.settings import BASE_DIR

CHROMEDRIVER_NAME = 'chromedriver'
CHROMEDRIVER_PATH = BASE_DIR / 'bin' / CHROMEDRIVER_NAME


def make_chrome_browser(*options):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')

    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    chrome_service = Service(executable_path=str(CHROMEDRIVER_PATH))
    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
    return browser
