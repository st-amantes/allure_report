import allure
from allure_commons.types import Severity
from selene import browser, be
from selene.support import by
from selene.support.shared.jquery_style import s

"""1 Чистый тест"""


def test_github():
    browser.open('https://github.com')
    s('.js-site-search-focus').click()
    s('.js-site-search-focus').send_keys('eroshenkoam/allure-example')
    s('.js-site-search-focus').submit()

    s(by.link_text('eroshenkoam/allure-example')).click()

    s('#issues-tab').click()

    s(by.partial_text('#76')).should(be.visible)


"""2 Лямбда щаги"""


def test_dinamic_github():
    with allure.step('Открываем главную страницу'):
        browser.open('https://github.com')

    with allure.step('Ищем репозиторий'):
        s('.js-site-search-focus').click()
        s('.js-site-search-focus').send_keys('eroshenkoam/allure-example')
        s('.js-site-search-focus').submit()

    with allure.step('Переходим по ссылке'):
        s(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Открываем таб Issues'):
        s('#issues-tab').click()

    with allure.step('Проверяем наличие Issue с номером 76'):
        s(by.partial_text('#76')).should(be.visible)


"""3 Щаги с декораторами"""


def test_static_github():
    open_main_page()
    search_repository('eroshenkoam/allure-example')
    go_repository('eroshenkoam/allure-example')
    open_issue_tab()
    should_see_issue_number('#76')


@allure.step('Открываем главную страницу')
def open_main_page():
    browser.open('https://github.com')


@allure.step('Ищем репозиторий {repo}')
def search_repository(repo):
    s('.js-site-search-focus').click()
    s('.js-site-search-focus').send_keys(repo)
    s('.js-site-search-focus').submit()


@allure.step('Переходим по ссылке {repo}')
def go_repository(repo):
    s(by.link_text(repo)).click()


@allure.step('Открываем таб Issues')
def open_issue_tab():
    s('#issues-tab').click()


@allure.step('Проверяем наличие Issue с номером 76')
def should_see_issue_number(number):
    s(by.partial_text(number)).should(be.visible)




"""4 Шаги с аннотациями"""
def test_dinamic_labels_github():
    allure.dynamic.tag('web')
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature('Задачи в репозитории')
    allure.dynamic.story('Неавторизованный пользователь не может создать задачу в репозитории')
    allure.dynamic.link('https://github.com', name='Testing')


@allure.tag('critical')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Vitalll')
@allure.feature('Задачи')
@allure.story('Авторизованный пользователь может создать задачу в репозитории')
@allure.link('https://github.com', name='Testing')
def test_decorator_github():
    pass
