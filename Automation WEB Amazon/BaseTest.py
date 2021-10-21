import time

from selenium import webdriver
import unittest


class BaseTest(unittest. TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):

        self.driver.close()
        self.driver.quit()