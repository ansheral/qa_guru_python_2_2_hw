import pytest
from selene.support.shared import browser
from selene import be, have

@pytest.fixture()
def open_browser():
    browser.open('https://google.com')


def test_search(open_browser):
    browser.element('[name="q"]').should(be.blank).type('selene python').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
