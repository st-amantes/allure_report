from selene import browser, by, be
from selene.support.shared.jquery_style import s
def test_github():
    browser.open('https://github.com')
    s('.js-site-search-focus').click()
    s('.js-site-search-focus').send_keys('eroshenkoam/allure-example')
    s('.js-site-search-focus').submit()

    s(by.link_text('eroshenkoam/allure-example')).click()

    s('#issues-tab').click()

    s(by.partial_text('#76')).should(be.visible)





