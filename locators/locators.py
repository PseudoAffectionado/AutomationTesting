from selenium.webdriver.common.by import By

# Common locators
last_page_locator = By.XPATH, '(//*[@class="tm-pagination__page"])[last()]'
article_locator = By.CLASS_NAME, 'tm-articles-list__item'
search_button_locator = By.CLASS_NAME, 'tm-header-user-menu__search'

# Main Page
services_dropdown_button = By.CLASS_NAME, 'tm-header__dropdown-toggle'
services_dropdown_element = By.CLASS_NAME, 'tm-our-projects__item'
navigation_dropdown_button = By.XPATH, '//*[contains(@data-test-id, "nav-filters-button")]'
navigation_dropdown_show = By.XPATH, '//*[contains(@class, "tm-navigation-filters__option")]' \
                                     '//*[contains(text(), "Лучшие")]'
navigation_dropdown_period = By.XPATH, '//*[contains(@class, "tm-navigation-filters__option")]' \
                                       '//*[contains(text(), "Год")]'
navigation_apply_button = By.XPATH, '//*[contains(@data-test-id, "nav-filters-apply")]'

# Search Page
search_icon_locator = By.CSS_SELECTOR, 'span.tm-search__icon'
search_input_locator = By.CLASS_NAME, 'tm-input-text-decorated__input'
empty_res_locator = By.XPATH, '//*[@class="tm-empty-placeholder__text"]'

# Feedback Page
submit_button = By.XPATH, '//*[contains(@class, "tm-form__submit")]'
email_error = By.XPATH, '//*[contains(@class, "base-input__error_email")]'
message_error = By.XPATH, '//*[contains(@class, "base-input__error_message")]'
agreement_error = By.XPATH, '//*[contains(@class, "base-checkbox__error_personalagreement")]'
subject_option = By.CSS_SELECTOR, 'select[name="themeId"] option'
subject = By.NAME, 'themeId'
