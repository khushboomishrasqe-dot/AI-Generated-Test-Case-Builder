import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.login_page import LoginPage


@pytest.fixture
def driver():
    options = Options()
    if os.getenv("HEADLESS", "false").lower() == "true":
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1440,1000")

    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()


def test_login_with_valid_credentials_opens_inventory(driver):
    """TC_LOGIN_001: A standard user can log in with valid credentials."""
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    assert "/inventory.html" in driver.current_url
    assert login_page.inventory_is_visible()
