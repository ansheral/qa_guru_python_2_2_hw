import pytest
from selene.support.shared import browser


@pytest.fixture()
def set_browser(open_browser):
    browser.config.window_width, browser.config.window_height = 1500, 1500


@pytest.fixture()
def open_browser():
    browser.open('https://google.com')
