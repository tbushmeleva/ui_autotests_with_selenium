import pytest

from pages.main_page import Main_page

@pytest.mark.main_page
def test_pulling_feed_scrollbar(set_up):
    mp = Main_page(set_up)
    mp.scroll_feed_scrollbar()