from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time

from Home.Pages import HomePage
from Home.Locator import Locators
from Home.Testdata import Testdata


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

class HomeTest(BaseTest):

    def test_click_electronics(self):
        self.Home_page = HomePage(self.driver)
        self.Home_page.click_electronics()
        time.sleep(3)

    def test_click_camera(self):
        self.Home_page = HomePage(self.driver)
        self.Home_page.click_camera()
        time.sleep(3)

    def test_click_accessories(self):
        self.Home_page = HomePage(self.driver)
        self.Home_page.click_accessories()
        time.sleep(3)

    def test_search_valid(self):
        self.Home_page = HomePage(self.driver)
        self.Home_page.search_valid()
        time.sleep(3)