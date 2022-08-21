from page import *


def test_empy_search(driver):
    page = MainPage(driver)
    page.open()
    page = page.click_search()
    page.search('qwertyasdfgh')
    page.count_articles_number()
    page.get_empty_page_text()
