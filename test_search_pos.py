from selene.support.shared import browser
from selene import be, have


def test_search(open_browser):
    browser.element('[name="q"]').should(be.blank).type('selene python').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
