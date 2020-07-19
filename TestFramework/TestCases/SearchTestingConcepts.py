from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import unittest
from TestFramework.Pages.HomePage import HomePage


class SearchTestingConcepts(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = Options()
        options.add_argument("--disable-notifications")
        cls.driver = webdriver.Chrome(executable_path="C:/Users/Chaos Virus/PycharmProjects/CodeChallenge/Drivers"
                                                      "/chromedriver.exe", options=options)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_searching_concepts(self):
        driver = self.driver
        searchbar = HomePage(driver)
        searchbar.search_criteria_search_bar('Testing Concepts' + Keys.ENTER)
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

