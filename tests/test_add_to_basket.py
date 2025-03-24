import pytest

from pages.basket_page import Basket_page
from pages.main_page import Main_page
from pages.search_result_page import Search_result_page
from pages.sign_in_page import Sign_in_page


@pytest.mark.smoke
def test_add_product_to_basket_from_search_page(set_up):
    mp = Main_page(set_up)
    mp.searching()

    srp = Search_result_page(set_up)
    srp.add_to_basket()
    search_page_price = srp.remember_product_price()
    search_page_name = srp.remember_product_name()

    bp = Basket_page(set_up)
    bp.open_basket_page()
    basket_page_name = bp.remember_product_name()
    basket_page_price = bp.remember_product_price()
    basket_subtotal_price = bp.remember_basket_subtotal_price()
    bp.assert_data_equality(search_page_name, basket_page_name)
    bp.assert_data_equality(search_page_price, basket_page_price)
    bp.assert_data_equality(basket_page_price, basket_subtotal_price)
    bp.open_checkout_page()

    sip = Sign_in_page(set_up)
    sip.open_sign_in_form()

@pytest.mark.smoke
def test_add_two_products_to_basket_and_compare_price(set_up):
    mp = Main_page(set_up)
    mp.searching()

    srp = Search_result_page(set_up)
    srp.add_to_basket()

    bp = Basket_page(set_up)
    bp.open_basket_page()
    basket_product_price = bp.remember_product_price()
    subtotal_price_before = bp.remember_basket_subtotal_price()
    bp.assert_data_equality(basket_product_price, subtotal_price_before)
    bp.increment_product()
    subtotal_price_after = bp.remember_basket_subtotal_price()
    products_price_summ = bp.summ_subtotal_price(basket_product_price, basket_product_price)
    bp.assert_data_equality(products_price_summ, subtotal_price_after)
    bp.open_checkout_page()







