from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Basket_page(Base):


    def __init__(self, browser):
        super().__init__(browser)
        self.actions = ActionChains(browser)


    #Locators

    basket_button = '[class="a-button a-button-span11 a-button-base a-button-small"]'
    button_checkout = '[data-feature-id="proceed-to-checkout-action"]'
    product_price = '//span[@data-a-size="b"]//span[@aria-hidden="true"]'
    product_name = '(//span[@class="a-truncate-cut"])[1]'
    subtotal_price = '(//span[@class="a-size-medium a-color-base sc-price sc-white-space-nowrap"])[2]'
    button_share = '[data-action="share"]'
    button_pinterest = '[aria-label="Pinterest"]'
    button_see_more = '(//span[contains(@id, "comparison")])[1]'
    more_items_popover = '[class="a-popover-wrapper"]'
    add_to_basket_more_items_popover = '(//span[@class="a-button a-spacing-top-small a-button-primary comparison_scroller_atc_row"])[1]'
    subtotal_items = '(//span[@id="sc-subtotal-label-activecart"])[1]'
    button_close_popover = '[class="a-icon a-icon-close"]'
    button_increment_product = '[data-a-selector="increment-icon"]'
    button_decrement_product = '[data-a-selector="decrement-icon"]'
    empty_cart_text = '[class="a-size-large a-spacing-top-base sc-your-amazon-cart-is-empty"]'
    product_counter_value = '[data-a-selector="value"]'


    #Getters

    def get_basket_button(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.basket_button)))

    def get_button_checkout(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.button_checkout)))

    def get_product_price(self):
        return WebDriverWait(self.browser, 30).until(EC.presence_of_element_located((By.XPATH, self.product_price)))

    def get_product_name(self):
        return WebDriverWait(self.browser, 30).until(EC.presence_of_element_located((By.XPATH, self.product_name)))

    def get_subtotal_price(self):
         return WebDriverWait(self.browser, 30).until(EC.presence_of_element_located((By.XPATH, self.subtotal_price)))

    def get_button_share(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.button_share)))

    def get_button_pinterest(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.button_pinterest)))

    def get_button_see_more(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_see_more)))

    def get_more_items_popover(self):
        return WebDriverWait(self.browser, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.more_items_popover)))

    def get_add_to_basket_more_items_popover(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_basket_more_items_popover)))

    def get_subtotal_items(self):
        return WebDriverWait(self.browser, 30).until(EC.visibility_of_element_located((By.XPATH, self.subtotal_items)))

    def get_button_close_popover(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.button_close_popover)))

    def get_button_increment_product(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.button_increment_product)))

    def get_button_decrement_product(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.button_decrement_product)))

    def get_empty_cart_text(self):
        return WebDriverWait(self.browser, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.empty_cart_text)))

    def get_product_counter_value(self):
        return WebDriverWait(self.browser, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.product_counter_value)))

    #Actions

    def click_basket_button(self):
        self.get_basket_button().click()
        print('Click basket icon')

    def click_button_checkout(self):
        self.get_button_checkout().click()
        print('Click "Proceed to checkout" button')

    def click_button_share(self):
        self.get_button_share().click()
        print('Click button Share')

    def click_button_pinterest(self):
        self.get_button_pinterest().click()
        print('Click Pinterest button')

    def click_button_see_more(self):
        self.get_button_see_more().click()
        print('Click button See more like this')

    def click_add_to_basket_button(self):
        self.get_add_to_basket_more_items_popover().click()
        print('Click button Add to basket')

    def click_button_close_popover(self):
        self.get_button_close_popover().click()
        print('Click button close popover')

    def click_button_increment_product(self):
        self.get_button_increment_product().click()
        print('Click increment button')

    def click_button_decrement_product(self):
        self.get_button_decrement_product().click()
        print('Click decrement button')


    #Methods

    def open_basket_page(self):
        self.click_basket_button()
        self.assert_url_contains('/cart')

    def open_checkout_page(self):
        self.click_button_checkout()

    def remember_product_price(self):
        return self.remember_price(self.get_product_price())

    def remember_product_name(self):
        return self.get_product_name().text

    def remember_basket_subtotal_price(self):
        return self.remember_price(self.get_subtotal_price())

    def share_cart_pinterest(self):
        self.click_button_share()
        self.click_button_pinterest()
        self.switch_to_browser_window(1)
        self.assert_url_contains('https://www.pinterest.com/')

    def add_product_from_more_popover(self):
        self.click_button_see_more()
        self.get_more_items_popover()
        self.click_add_to_basket_button()
        self.click_button_close_popover()
        self.get_subtotal_items()
        self.assert_word_contains(self.get_subtotal_items(), 'Subtotal (2 items):')

    def empty_cart(self):
        self.click_button_decrement_product()
        self.browser.refresh()
        self.assert_word_contains(self.get_empty_cart_text(), 'Cart is empty')

    def increment_product(self):
        self.click_button_increment_product()
        self.assert_word(self.get_product_counter_value(), '2')











