import pytest
from selenium import webdriver


@pytest.fixture()
def set_up():
    print('Start test')
    browser = webdriver.Chrome()
    link = 'https://www.amazon.co.uk/'
    browser.get(link)
    browser.maximize_window()
    yield browser
    browser.quit()
    print('Finish test')


