# Imports needed for webdriver explicit waits
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    def __init__(self, driver):
        self.driver = driver

        # Store all element locators of the page in a variable for reference and ease of maintenance
        self.search_bar_id = 'header-search-bar'
        self.user_account_id = 'USER_DROPDOWN_ID'
        self.night_mode_class_name = '_3m4MQxMy4WfgIkMhHh-UAg'
        self.home_icon_class_name = '_1O4jTk-dZ-VIxsCuYB6OR8'
        self.home_background_class_name = '_1VP69d9lk-Wk9zokOaylL'

    def click_user_account(self):
        self.driver.find_element_by_id(self.user_account_id).click()

    def toggle_night_mode_on(self):
        self.driver.find_element_by_class_name(self.night_mode_class_name).click()
        nighton = self.driver.find_element_by_class_name(self.home_background_class_name).get_attribute('style')
        assert nighton == '--background:#1A1A1B; --canvas:#030303;'

    def toggle_night_mode_off(self):
        self.driver.find_element_by_class_name(self.night_mode_class_name).click()
        nightoff = self.driver.find_element_by_class_name(self.home_background_class_name).get_attribute('style')
        assert nightoff == '--background:#FFFFFF; --canvas:#DAE0E6;'
        title = self.driver.current_url
        assert title == 'https://www.reddit.com/'

    def search_criteria_search_bar(self, criteria):
        # Clear the field to avoid errors with remaining text
        self.driver.find_element_by_id(self.search_bar_id).clear()
        self.driver.find_element_by_id(self.search_bar_id).send_keys(criteria)

        # This is needed to wait until the element is loaded and available for interaction with a timeout of 5 seconds
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'rpBJOHq2PR60pnwJlUyP0'))
            )
        except:
            # In case the element doesnt load in 7 seconds the webdriver will completely end and the test will fail
            self.driver.quit()

    def click_home_icon(self):
        self.driver.find_element_by_class_name(self.home_icon_class_name).click()
        # This is needed to wait until the element is loaded and available for interaction with a timeout of 5 seconds
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'rpBJOHq2PR60pnwJlUyP0'))
            )
        except:
            # In case the element doesnt load in 7 seconds the webdriver will completely end and the test will fail
            self.driver.quit()
