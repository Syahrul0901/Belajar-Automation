from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains

    def alert_js(self):
        WebDriverWait(self.driver, 3000).until(
            EC.alert_is_present()
        )

    # function input data
    def enter_text(self, locator, teks):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).send_keys(teks)

    # function click Locator
    def click(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).click()

    # function delete data
    def clear_text(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).clear()

    # function get text
    def get_text(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        ).text

    def get_toast(self, locator):
        get_toast = self.driver.find_element(locator)
        return get_toast.get_attribut("innerHTML")

    # function check element visible
    def is_visible(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator))
            return bool(element)
        except TimeoutException:
            return False

    # function select single drop down by index
    def select_single_dropdown_by_index(self, locator, item):
        dropdown = Select(self.driver.find_element_by_id(locator))
        dropdown.select_by_index(item)

    # function select multi drop down aa
    def select_single_dropdown_by_class(self, locator, item):
        dropdown = Select(self.driver.find_element_by_class(locator))
        dropdown.select_by_index(item)

    # function select dropdown
    def select_dropdown_by_value(self, locator, item):
        dropdown = Select(self.driver.find_element_by_id(locator))
        dropdown.select_by_value(item)

    def select_dropdown_by_xpath(self, locator, item):
        dropdown = Select(self.driver.find_element_by_xpath(locator))
        dropdown.select_by_value(item)

    def select_dropdown_by_visible_text(self, locator, item):
        dropdown = Select(self.driver.find_element_by_id(locator))
        dropdown.select_by_visible_text(item)

    def select_multiple_list(self, locator, item):
        dropdown = Select(self.driver.find_element_by_id(locator))
        dropdown.select_by_visible_text(item)

    # function hover
    def move_element_to(self, locator):
        hover = self.driver.find_element_by_xpath(locator)
        self.action.move_to_element(hover).perform()

    # function click js alert
    def alert_click(self, locator):
        self.driver.find_element_by_xpath(locator).click()
        jsalert = self.driver.switch_to.alert.accept()
        return jsalert.get_attribute("validationMessage")

    def alert_js_validation(self):
        email_input = self.driver.find_element_by_id("email")
        return email_input.get_attribute("validationMessage")


