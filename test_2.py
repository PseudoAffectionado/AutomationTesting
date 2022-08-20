from page import *


def test_empy_search(driver):
    click_search_form(driver)
    type_text(driver, 'qwertyadfgh')
    click_search_form(driver)
    click_search_button(driver)
    count_articles_number(driver)

    check_empty_page_text(driver)
