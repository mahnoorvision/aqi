import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()
    # REMOVE headless mode for debugging
    # options.add_argument('--headless')  # COMMENT THIS OUT
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
