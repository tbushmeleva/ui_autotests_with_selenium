import datetime
from selenium.webdriver import ActionChains


class Base():

    def __init__(self, browser):
        self.browser = browser
        self.actions = ActionChains(browser)


    #Method for getting current url
    def get_current_url(self):
        get_url = self.browser.current_url
        print(f'Current url is "{get_url}"')

    #Method for getting text and compare it with the expected one. The text must match completely.
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print(f'value_word is "{value_word}"')
        print('Good value word')

    #Method for getting text and compare it with the expected one. The text may partially match.
    def assert_word_contains(self, word, result):
        value_word = word.text
        assert result in value_word
        print(f'value_word is "{value_word}"')
        print('Good value word')

    #Method for making screenshot
    def get_screenshot(self):
        now_date = datetime.datetime.now()
        name_screenshot = 'screenshot' + str(now_date) + '.png'
        self.browser.save_screenshot('/Users/tatyanabushmeleva/PycharmProjects/python_selenium_autotests_ui/screens/' + name_screenshot)

    #Method for getting current url and compare it with the expected one. The text must match completely.
    def assert_url(self, result):
        get_url = self.browser.current_url
        assert result == get_url
        print('Good value url')

    #Method for getting current url and compare it with the expected one. The text may partially match.
    def assert_url_contains(self, result):
        get_url = self.browser.current_url
        assert result in get_url
        print('Good value url')

    #Method for scrolling to the element
    def scroll_to_element(self, element):
        self.actions.move_to_element(element).perform()
        print('Scroll to element')

    #Method for interacting with the sliders
    def pull_slider(self, slider, x_offset, y_offset):
        self.actions.click_and_hold(slider).move_by_offset(x_offset, y_offset).release().perform()
        print('Pull slider')

    #Method for switching between browser tabs
    def switch_to_browser_window(self, window_index):
        windows = self.browser.window_handles
        self.browser.switch_to.window(windows[window_index])

    #Method for make sure ath element is selected
    def assert_element_is_selected(self, element, result):
        element = element.is_selected()
        assert element == result
        print(f'Element selection is {result}')

    #Method for parcing product's price. WIl be reused on different pages/places
    def remember_price(self, element):
        price = element.text
        price_value = price.strip("£").replace(',', '')
        print(f'Price value is {price_value}')
        return float(price_value)

    #Method for comparing data. Data must match completely.
    def assert_data_equality(self, expectation, result):
        assert expectation == result
        print('Data equals')

    #Method for comparing data. Data must not match completely.
    def assert_data_inequality(self, expectation, result):
        assert expectation != result
        print('Data is not equals')

    #Method for calculating total price in the basket
    def summ_subtotal_price(self, price_one, price_two):
         subtotal_price_summ = float(price_one) + float(price_two)
         print(f'Subtotal price summ is {subtotal_price_summ}')
         return subtotal_price_summ








