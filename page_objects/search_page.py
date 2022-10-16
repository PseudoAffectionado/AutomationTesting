import time

from locators.locators import search_input_locator, search_icon_locator, empty_res_locator
from page_objects.base_page import HabrBase


class SearchPage(HabrBase):
    url = 'https://habr.com/ru/search'

    @property
    def search_input(self):
        return self.webdriver.find_element(*search_input_locator)

    @property
    def search_button(self):
        return self.webdriver.find_element(*search_icon_locator)

    def search(self, search_text):
        self.search_input.send_keys(search_text)
        self.search_button.click()
        time.sleep(1)

    def is_page_shown(self):
        return self.search_input.is_displayed()

    @property
    def empty_result_banner(self):
        return self.webdriver.find_element(*empty_res_locator)

    def get_empty_page_text(self):
        return self.empty_result_banner.text
