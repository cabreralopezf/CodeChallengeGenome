from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from TestFramework.Pages.HomePage import HomePage
from TestFramework.Pages.SearchResultsPage import SearchResultsPage
# from TestFramework.Configurations.ChromeDriverSetup import ChromeDriverSetup
import time
import os
import unittest


class AllScenarios(unittest.TestCase):

    # This method initiates the webdriver, provides the webdriver location and execution options
    @classmethod
    def setUpClass(cls):
        # setup = ChromeDriverSetup()
        # setup.chrome_setup()
        options = Options()
        options.add_argument("--disable-notifications")
        path = os.path.dirname(os.path.realpath(__file__)).rsplit(os.sep, 2)[0]
        cls.driver = webdriver.Chrome(executable_path=path + "/Drivers/chromedriver.exe", options=options)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_all_scenarios_challenge(self):
        driver = self.driver
        # Enter the reddit website to start the test
        driver.get("https://www.reddit.com/")

        # All events needed to toggle on the Night Mode button
        home = HomePage(driver)
        home.click_user_account()
        home.click_night_mode()
        print('Test Night Mode On Completed')

        # Inputs sent to the Text Box to search for the Testing Concepts criteria
        home.search_criteria_search_bar('Testing Concepts' + Keys.ENTER)

        # This is needed to wait until the element is loaded and available for interaction with a timeout of 7 seconds
        try:
            element = WebDriverWait(driver, 7).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'rpBJOHq2PR60pnwJlUyP0'))
            )
        except:
            # In case the element doesnt load in 7 seconds the webdriver will completely end and the test will fail
            driver.quit()

        # Events to Open the search result in a new tab, focus the tab then switch back to the previous tab
        results = SearchResultsPage(driver)
        results.open_new_tab_search_result()

        # This sleep allows a chance for visibility of the event, this can be removed for efficiency
        time.sleep(2)

        # Switch to the starting tab
        self.driver.switch_to.window(self.driver.window_handles[0])

        # Events for clicking the home icon and verifying the user is in the correct home page
        home.click_home_icon()
        title = self.driver.current_url
        self.assertEqual(title, 'https://www.reddit.com/', 'Website is different from https://www.reddit.com/')

        # This is needed to wait until the element is loaded and available for interaction with a timeout of 7 seconds
        try:
            element = WebDriverWait(driver, 7).until(
                EC.presence_of_element_located((By.ID, 'USER_DROPDOWN_ID'))
            )
        except:
            # In case the element doesnt load in 7 seconds the webdriver will completely end and the test will fail
            driver.quit()

        # All events needed to toggle off the Night Mode button
        home.click_user_account()
        home.click_night_mode()

        # This sleep allows a chance for visibility of the event, this can be removed for efficiency
        time.sleep(2)
        print('Test Cases Completed')

    # This method is called on completion of the test case and closes the tabs and closes the webdriver instance
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")
