import time

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Search_result_page(Base):


    def __init__(self, browser):
        super().__init__(browser)
        self.actions = ActionChains(browser)


    #Locators

    button_add_to_basket = '(//button[@name="submit.addToCart"])[1]'
    product_price = '//span[@class="a-size-base a-text-bold"]'
    product_name = '(//a[@class="a-link-normal s-line-clamp-2 s-link-style a-text-normal"])[1]//h2//span'
    basket_counter = '(//span[@class="a-dropdown-prompt"])[1]'
    filter_sort_by = '[data-action="a-dropdown-button"]'
    filter_sort_by_select = '[id="s-result-sort-select_5"]'
    category_select = '[id="searchDropdownBox"]'
    search_field_input = '[id="twotabsearchtextbox"]'
    link_see_more = '(//span[@class="a-expander-prompt"])[1]'
    brand_checkbox_1 = '//li[@id="p_123/46655"]//i[@class="a-icon a-icon-checkbox"]' #Samsung
    brand_checkbox_2 = '//li[@id="p_123/237204"]//i[@class="a-icon a-icon-checkbox"]' #Sony
    button_clear_filters = '[class="a-link-normal s-navigation-item s-navigation-clear-link"]'
    pagination_next_button = '//a[contains(@class, "s-pagination-next")]'
    pagination_previous_button = '//a[contains(@class, "s-pagination-previous")]'


    #Getters

    def get_button_add_to_basket(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_add_to_basket)))

    def get_basket_counter(self):
        return WebDriverWait(self.browser, 30).until(EC.presence_of_element_located((By.XPATH, self.basket_counter)))

    def get_product_price(self):
        return WebDriverWait(self.browser, 30).until(EC.presence_of_element_located((By.XPATH, self.product_price)))

    def get_product_name(self):
        return WebDriverWait(self.browser, 30).until(EC.presence_of_element_located((By.XPATH, self.product_name)))

    def get_filter_sort_by(self):
         return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.filter_sort_by)))

    def get_filter_sort_by_select(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.filter_sort_by_select)))

    def get_category_select(self):
        return Select(WebDriverWait(self.browser, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.category_select))))

    def get_search_field_input(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.search_field_input)))

    def get_link_see_more(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_see_more)))

    def get_brand_checkbox_1(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.brand_checkbox_1)))

    def get_brand_checkbox_2(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.brand_checkbox_2)))

    def get_button_clear_filters(self):
        return WebDriverWait(self.browser, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.button_clear_filters)))

    def get_pagination_next_button(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.pagination_next_button)))

    def get_pagination_previous_button(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.pagination_previous_button)))


    #Actions

    def click_button_add_to_basket(self):
        self.get_button_add_to_basket().click()
        print('Click button "Add to basket')

    def apply_filter_sort_by(self):
        self.get_filter_sort_by().click()
        self.get_filter_sort_by_select().click()
        print('Click filter "Sort by"')

    def select_category_select(self):
        self.get_category_select().select_by_value('search-alias=electronics')
        self.get_search_field_input().send_keys(Keys.RETURN)
        print('Select category select')

    def click_link_see_more(self):
        self.get_link_see_more().click()
        print('Click "See more"')

    def click_brand_checkboxes(self):
        self.get_brand_checkbox_2().click()
        self.get_brand_checkbox_1().click()
        print('Click brand checkboxes')

    def click_button_clear_filter(self):
        self.get_button_clear_filters().click()
        print('Click button "Clear"')

    def click_pagination_previous_button(self):
        self.get_pagination_previous_button().click()
        print('Click pagination previous button')

    def click_pagination_next_button(self):
        self.get_pagination_next_button().click()
        print('Click pagination next button')


    #Methods

    def add_to_basket(self):
        self.click_button_add_to_basket()
        time.sleep(1)
        self.assert_word(self.get_basket_counter(), '1')

    def remember_product_price(self):
        return self.remember_price(self.get_product_price())

    def remember_product_name(self):
        return self.get_product_name().text

    def choose_sorting(self):
        self.apply_filter_sort_by()
        self.assert_url_contains('s=exact-aware-popularity-rank')

    def choose_category_select(self):
        self.select_category_select()
        self.assert_url_contains('i=electronics')

    def choose_brand_checkboxes(self):
        self.click_link_see_more()
        self.click_brand_checkboxes()
        self.assert_url_contains('rh=')

    def clear_filters(self):
        self.get_brand_checkbox_1().click()
        self.click_button_clear_filter()
        self.assert_element_is_selected(self.get_brand_checkbox_1(), False)

    def pagination(self):
        self.click_pagination_next_button()
        self.assert_url_contains('page=2')
        self.click_pagination_previous_button()








