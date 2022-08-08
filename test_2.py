from page import *


def test_empy_search(driver):
    click_search_form(driver)
    type_text(driver, 'qwertyadfgh')
    click_search_form(driver)
    click_search_button(driver)
    count_articles_number(driver)

    check_empty_page_text(driver)


if __name__ == '__main__':
    driver_object = setup()
    try:
        test_empy_search(driver_object)
    except NoSuchElementException as error:
        print(f'Test failed, {error}')
    tear_down(driver_object)
