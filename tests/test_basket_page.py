from pages.basket_page import Basket_page
from pages.main_page import Main_page
from pages.search_result_page import Search_result_page


def test_sharing_cart_to_pinterest(set_up):
    mp = Main_page(set_up)
    mp.searching()

    srp = Search_result_page(set_up)
    srp.add_to_basket()

    bp = Basket_page(set_up)
    bp.open_basket_page()
    bp.share_cart_pinterest()

def test_add_product_from_comparison_popover(set_up):
    mp = Main_page(set_up)
    mp.searching()

    srp = Search_result_page(set_up)
    srp.add_to_basket()

    bp = Basket_page(set_up)
    bp.open_basket_page()
    bp.add_product_from_more_popover()

def test_remove_all_products(set_up):
    mp = Main_page(set_up)
    mp.searching()

    srp = Search_result_page(set_up)
    srp.add_to_basket()

    bp = Basket_page(set_up)
    bp.open_basket_page()
    bp.empty_cart()





