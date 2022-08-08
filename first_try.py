import time

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def setup():
    print('set up')
    driver = webdriver.WebDriver(executable_path='./chromedriver')
    driver.get('https://habr.com/ru/all/')
    time.sleep(1)
    return driver


def tear_down(driver):
    print('tear down')
    driver.quit()


def test_basic_search(driver):
    # Поиск поля поиска
    search_button_locator = By.CLASS_NAME, 'tm-header-user-menu__search'
    search_button = driver.find_element(*search_button_locator)
    search_button.click()
    time.sleep(1)

    # вбить текст
    search_input_locator = By.CLASS_NAME, 'tm-input-text-decorated__input'
    search_input = driver.find_element(*search_input_locator)
    text_to_search = 'asdfjkjf'
    search_input.send_keys(text_to_search)

    # нажать на иконку
    search_icon_locator = By.CSS_SELECTOR, 'span.tm-search__icon'
    search_icon = driver.find_element(*search_icon_locator)
    search_icon.click()
    time.sleep(3)

    # посчитать количество записей(20)
    article_locator = By.TAG_NAME, 'article'
    articles = driver.find_elements(*article_locator)
    print(f'Number of articles is {len(articles)}')

    # посчитать количество страниц(50)
    last_page_locator = By.XPATH, '(//*[@class="tm-pagination__page"])[last()]'
    last_page_number = driver.find_element(*last_page_locator)
    element_text = last_page_number.text
    print(f'Number of pages is {element_text}')


if __name__ == '__main__':
    driver = setup()
    try:
        test_basic_search(driver)
    except NoSuchElementException as error:
        print(f'Test failed, reason: {error}')

    tear_down(driver)
