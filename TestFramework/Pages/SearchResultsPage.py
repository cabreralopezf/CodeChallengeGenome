# Imports needed to handle action chains and simulate user ctrl + click input
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class SearchResultsPage:

    def __init__(self, driver):
        self.driver = driver

        # Store all element locators of the page in a variable for reference and ease of maintenance
        self.search_result_list_class = 'rpBJOHq2PR60pnwJlUyP0'
        self.search_result_list_index_class = '_1poyrkZ7g36PawDueRza-J'

    def open_new_tab_search_result(self):
        # Store the element in a variable for cleaner code
        element = self.driver.find_element_by_class_name(self.search_result_list_index_class)

        # Action Chain to input multiple key inputs together
        ActionChains(self.driver).key_down(Keys.CONTROL).click(element).key_up(Keys.CONTROL).perform()

        # This makes the tab to be manually focused since selenium does not switch focus automatically
        self.driver.switch_to.window(self.driver.window_handles[1])
        search_title = self.driver.current_url
        assert search_title != 'https://www.reddit.com/'
        self.driver.implicitly_wait(2)
        # Switch to the starting tab
        self.driver.switch_to.window(self.driver.window_handles[0])
