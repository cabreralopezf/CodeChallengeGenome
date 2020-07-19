from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os


class ChromeDriverSetup:
    def chrome_setup(self):
        options = Options()
        options.add_argument("--disable-notifications")
        path = os.path.dirname(os.path.realpath(__file__)).rsplit(os.sep, 2)[0]
        driver = webdriver.Chrome(executable_path=path + "/Drivers/chromedriver.exe", options=options)
        driver.implicitly_wait(10)
        driver.maximize_window()

