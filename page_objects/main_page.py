import time

from locators.locators import search_button_locator, services_dropdown_button, services_dropdown_element
from page_objects.base_page import HabrBase
from page_objects.search_page import SearchPage


class MainPage(HabrBase):
    url = 'https://habr.com'

    # services list
    HABR = 0
    QNA = 1
    CAREER = 2
    FL = 3

    @property
    def search_button(self):
        return self.webdriver.find_element(*search_button_locator)

    def click_search(self):
        time.sleep(1)
        self.search_button.click()
        time.sleep(1)

        return SearchPage(self.webdriver)

    def click_services_dropdown(self):
        element = self.webdriver.find_element(*services_dropdown_button)
        element.click()

    @property
    def services(self):
        return self.webdriver.find_elements(*services_dropdown_element)

    def click_external_service(self, service_index):
        assert service_index in (self.HABR, self.QNA, self.CAREER, self.FL)

        service_pages_map = {
            self.HABR: MainPage,
            self.QNA: QNAPage,
            self.CAREER: CareerPage,
            self.FL: FLPage
        }

        element = self.services[service_index]
        element.click()
        self.focus_on_new_tab()
        page_class = service_pages_map.get(service_index)
        return page_class(self.webdriver)


class CareerPage(HabrBase):
    url = 'https://career.habr.com/'


class QNAPage(HabrBase):
    url = 'https://qna.habr.com'


class FLPage(HabrBase):
    url = 'https://freelance.habr.com'
