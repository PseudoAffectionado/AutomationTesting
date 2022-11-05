from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import wait
from locators.locators import *
from page_objects.base_page import HabrBase
from page_objects.search_page import SearchPage, TopYearlyPage


class MainPage(HabrBase):
    url = 'https://habr.com/ru/all/'
    # services list
    HABR = 0
    QNA = 1
    CAREER = 2
    FL = 3

    @property
    def search_button(self):
        return self.webdriver.find_element(*search_button_locator)

    @property
    def services(self):
        return self.webdriver.find_elements(*services_dropdown_element)

    def wait_full_page(self):
        wait = WebDriverWait(self.webdriver, 5)
        wait.until(
            presence_of_element_located(article_locator)
        )

    def click_search(self):
        self.search_button.click()
        page = SearchPage(self.webdriver)

        page.wait_full_page()
        return page

    def click_services_dropdown(self):
        element = self.webdriver.find_element(*services_dropdown_button)
        element.click()

    def click_external_service(self, service_index):
        assert service_index in (self.HABR, self.QNA, self.CAREER, self.FL)
        service_pages_map = {
            self.HABR: MainPage,
            self.QNA: QNAPage,
            self.CAREER: CareerPage,
            self.FL: FLPage,
        }
        element = self.services[service_index]
        element.click()
        self.focus_on_new_tab()
        page_class = service_pages_map.get(service_index)
        return page_class(self.webdriver)

    def click_services_dropdown(self):
        element = self.webdriver.find_element(*services_dropdown_button)
        element.click()

    def click_external_service(self, service_index):
        assert service_index in (self.HABR, self.QNA, self.CAREER, self.FL)

        service_pages_map = {
            self.HABR: MainPage,
            self.QNA: QNAPage,
            self.CAREER: CareerPage,
            self.FL: FLPage,
        }

        element = self.services[service_index]
        element.click()

        self.focus_on_new_tab()
        page_class = service_pages_map.get(service_index)
        return page_class(self.webdriver)

    def click_nav_button(self):
        element = self.webdriver.find_element(*navigation_dropdown_button)
        element.click()
        wait = WebDriverWait(self.webdriver, 5)
        wait.until(element_to_be_clickable(navigation_dropdown_show))

    def click_nav_options(self):
        first_show_element = self.webdriver.find_element(*navigation_dropdown_show)
        first_show_element.click()
        period_element = self.webdriver.find_element(*navigation_dropdown_period)
        period_element.click()

    def click_apply_button(self):
        element = self.webdriver.find_element(*navigation_apply_button)
        element.click()
        page = TopYearlyPage(self.webdriver)
        page.wait_full_page()
        return page


class CareerPage(HabrBase):
    url = 'https://career.habr.com/'


class QNAPage(HabrBase):
    url = 'https://qna.habr.com/'


class FLPage(HabrBase):
    url = 'https://freelance.habr.com/'
