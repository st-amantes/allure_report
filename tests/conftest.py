from selene import browser

import pytest


@pytest.fixture(scope='function', autouse=True)
def browser_managment():
    browser.driver.set_window_size(1920, 1080)
    browser.config.base_url = 'https://github.com/'
