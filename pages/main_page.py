from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Main_page(Base):

    def __init__(self, browser):
        super().__init__(browser)

    #Locators

    button_decline_cookie = '[id="sp-cc-rejectall-link"]'
    button_location_dismiss = '[data-action-type="DISMISS"]'
    search_field_input = '[id="twotabsearchtextbox"]'
    result_text = '[class="a-color-state a-text-bold"]'
    search_suggestion = '(//div[contains(@class, "s-suggestion-ellipsis-direction")])[1]//span'
    search_container = '[class="nav-search-field "]'
    main_logo = '[id="nav-logo-sprites"]'
    button_delete_search_suggestion = '[class="s-suggestion-deleteDistinct"]'
    feed_carousel = '[class="a-section a-spacing-none feed-carousel first-carousel"]'
    feed_scrollbar = '[class="feed-scrollbar-thumb"]'
    sign_in_menu = '[class="nav-line-2 "]'
    button_sign_in = '[class="nav-action-inner"]'

    #Getters

    def get_button_decline_cookie(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.button_decline_cookie)))

    def get_button_location_dismiss(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.button_location_dismiss)))

    def get_search_field(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.search_field_input)))

    def get_search_suggestion(self):
         return WebDriverWait(self.browser, 30).until(EC.visibility_of_element_located((By.XPATH, self.search_suggestion)))

    def get_result_text(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.result_text)))

    def get_search_container(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.search_container)))

    def get_main_logo(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.main_logo)))

    def get_button_delete_search_suggestion(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.button_delete_search_suggestion)))

    def get_feed_scrollbar(self):
        return WebDriverWait(self.browser, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.feed_scrollbar)))

    def get_feed_carousel(self):
        return WebDriverWait(self.browser, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.feed_carousel)))

    def get_sign_in_menu(self):
        return WebDriverWait(self.browser, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.sign_in_menu)))

    def get_button_sign_in(self):
        return WebDriverWait(self.browser, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.button_sign_in)))


    #Actions

    def click_decline_cookie(self):
        self.get_button_decline_cookie().click()
        print('Click Decline cookie button')

    def click_location_dismiss(self):
        self.get_button_location_dismiss().click()
        print('Click Dismiss button')

    def execute_search_field_input(self, request):
        self.get_search_field().send_keys(request)
        self.get_search_field().send_keys(Keys.RETURN)
        print('Execute search input')

    def fill_search_field_input(self, request):
        self.get_search_field().send_keys(request)
        print('Fill search input')

    def click_search_field_input(self):
        self.get_search_field().click()
        print('Click search input')

    def click_search_container(self):
        self.get_search_container().click()
        print('Click search field')

    def click_search_suggestion(self):
        self.get_search_suggestion().click()
        print('Click search suggestion')

    def click_main_logo(self):
        self.get_main_logo().click()
        print('Click main logo')

    def click_button_delete_search_suggestion(self):
        self.get_button_delete_search_suggestion().click()
        print('Click button delete search suggestion')

    def click_sign_in_menu(self):
        self.get_sign_in_menu().click()
        print('Click Sign in menu')

    def click_button_sign_in(self):
        self.get_button_sign_in().click()
        print('Click Sign in button ')

    #Methods

    def searching(self):
        self.click_decline_cookie()
        self.click_location_dismiss()
        self.execute_search_field_input('phone')
        self.assert_word(self.get_result_text(), '"phone"')

    def search_suggestions(self):
        self.click_decline_cookie()
        self.click_location_dismiss()
        self.fill_search_field_input('phone')
        self.assert_word_contains(self.get_search_suggestion(), 'phone')
        self.click_search_suggestion()
        self.assert_word_contains(self.get_result_text(), 'phone')

    def delete_search_suggestion(self):
        self.click_decline_cookie()
        self.click_location_dismiss()
        self.execute_search_field_input('phone')
        self.click_main_logo()
        self.assert_url_contains('ref=nav_logo')
        self.click_search_field_input()
        self.assert_word_contains(self.get_search_suggestion(), 'phone')
        self.get_button_delete_search_suggestion()

    def scroll_feed_scrollbar(self):
        self.click_decline_cookie()
        self.click_location_dismiss()
        self.scroll_to_element(self.get_feed_carousel())
        self.get_screenshot()
        self.pull_slider(self.get_feed_scrollbar(), 300, 0)
        self.get_screenshot()

    def open_sign_in_page(self):
        self.click_decline_cookie()
        self.click_location_dismiss()
        self.click_sign_in_menu()
        self.assert_url_contains('signin')






