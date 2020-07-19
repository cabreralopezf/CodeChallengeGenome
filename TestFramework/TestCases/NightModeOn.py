from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import unittest
from TestFramework.Pages.HomePage import HomePage


class NightModeOn(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = Options()
        options.add_argument("--disable-notifications")
        cls.driver = webdriver.Chrome(executable_path="C:/Users/Chaos Virus/PycharmProjects/CodeChallenge/Drivers"
                                                      "/chromedriver.exe", options=options)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_night_mode_on(self):
        driver = self.driver
        driver.get("https://www.reddit.com/")
        nightmode = HomePage(driver)
        nightmode.click_user_account()
        nightmode.click_night_mode()
        time.sleep(2)
        print('Test Night Mode On Completed')

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")
