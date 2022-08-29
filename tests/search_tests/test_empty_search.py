from page_objects.page import *


def test_empy_search(driver):
    page = MainPage(driver)
    page.open()

    page = page.click_search()
    page.search('qwertyasdfgh')

    assert page.count_articles_number() == 0


def test_empty_search_text(driver):
    page = MainPage(driver)
    page.open()

    page = page.click_search()
    page.search('qwertyasdfgh')

    assert len(page.get_empty_page_text()) > 0