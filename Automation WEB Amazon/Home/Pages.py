import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from Home.Testdata import Testdata
from Home.Locator import Locators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains

     # function input data
    def enter_text(self, locator, teks):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).send_keys(teks)

    def get_text(self, locator):

        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        ).text

    # function click Locator
    def move_element_to(self, locator):
        hover = self.driver.find_element_by_xpath(locator)
        self.action.move_to_element(hover).perform()

    def click(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).click()

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(Testdata.BASE_URL)

    def click_electronics(self):
        self.click(Locators.BUTTON_ALL)
        time.sleep(3)
        self.click(Locators.BUTTON_ELECTRONICS)
        time.sleep(3)
        self.click(Locators.BUTTON_TELEVISIONS_VIDEO)
        time.sleep(2)
        self.click(Locators.BUTTON_TELEVISIONS)
        time.sleep(2)
        self.click(Locators.BUTTON_TEXT)
        time.sleep(2)

    def click_camera(self):
        self.click(Locators.BUTTON_ALL)
        time.sleep(3)
        self.click(Locators.BUTTON_ELECTRONICS)
        time.sleep(3)
        self.click(Locators.BUTTON_CAMERA_FOTO)
        time.sleep(2)
        self.click(Locators.BUTTON_LENSES)
        time.sleep(2)
        self.click(Locators.FIELD_LENSA)
        time.sleep(2)

    def click_accessories(self):
        self.click(Locators.BUTTON_ALL)
        time.sleep(3)
        self.click(Locators.BUTTON_ELECTRONICS)
        time.sleep(3)
        self.click(Locators.BUTTON_ACCESSORIES)
        time.sleep(2)
        self.click(Locators.BUTTON_BLANK_MEDIA)
        time.sleep(2)
        self.click(Locators.BUTTON_DVD_RW)
        time.sleep(2)
        self.click(Locators.FIELD_DVD_RW)
        time.sleep(2)
        
    def search_valid(self):
        self.enter_text(Locators.SEARCH_FIELD, Testdata.SEARCH_FIELD_DATA)
        time.sleep(2)
        self.click(Locators.SEARCH_RESULT)
        time.sleep(3)
        self.click(Locators.SEARCH_NAME)
        
        
