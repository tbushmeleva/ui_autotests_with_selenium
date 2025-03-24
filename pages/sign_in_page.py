from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Sign_in_page(Base):


    def __init__(self, browser):
        super().__init__(browser)
        self.actions = ActionChains(browser)


    #Locators

    sign_in_form = '[class="a-box-inner a-padding-extra-large"]'


    #Getters

    def get_sign_in_form(self):
        return WebDriverWait(self.browser, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.sign_in_form)))


    #Actions


    #Methods

    def open_sign_in_form(self):
        self.get_sign_in_form()
        self.assert_url_contains('/signin')










