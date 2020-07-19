class HomePage:

    def __init__(self, driver):
        self.driver = driver

        # Store all element locators of the page in a variable for reference and ease of maintenance
        self.search_bar_id = 'header-search-bar'
        self.user_account_id = 'USER_DROPDOWN_ID'
        self.night_mode_class_name = '_3m4MQxMy4WfgIkMhHh-UAg'
        self.home_icon_class_name = '_1O4jTk-dZ-VIxsCuYB6OR8'

    def click_user_account(self):
        self.driver.find_element_by_id(self.user_account_id).click()

    def click_night_mode(self):
        self.driver.find_element_by_class_name(self.night_mode_class_name).click()

    def search_criteria_search_bar(self, criteria):
        # Clear the field to avoid errors with remaining text
        self.driver.find_element_by_id(self.search_bar_id).clear()
        self.driver.find_element_by_id(self.search_bar_id).send_keys(criteria)

    def click_home_icon(self):
        self.driver.find_element_by_class_name(self.home_icon_class_name).click()

