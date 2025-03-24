import pytest

from pages.main_page import Main_page
from pages.search_result_page import Search_result_page

def test_search_for_a_product(set_up):
    mp = Main_page(set_up)
    mp.searching()

def test_working_with_search_suggestions(set_up):
    mp = Main_page(set_up)
    mp.search_suggestions()

def test_delete_search_suggestion(set_up):
    mp = Main_page(set_up)
    mp.delete_search_suggestion()

def test_apply_sorting(set_up):
    mp = Main_page(set_up)
    mp.searching()

    srp = Search_result_page(set_up)
    srp.choose_sorting()

def test_search_for_a_product_in_certain_category(set_up):
    mp = Main_page(set_up)
    mp.searching()

    srp = Search_result_page(set_up)
    srp.choose_category_select()

def test_apply_filter_checkboxes_brands(set_up):
    mp = Main_page(set_up)
    mp.searching()

    srp = Search_result_page(set_up)
    srp.choose_brand_checkboxes()

def test_clear_selected_filters(set_up):
    mp = Main_page(set_up)
    mp.searching()

    srp = Search_result_page(set_up)
    srp.clear_filters()

def test_pagination(set_up):
    mp = Main_page(set_up)
    mp.searching()

    srp = Search_result_page(set_up)
    srp.pagination()






