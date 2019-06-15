from selenium import webdriver

from pages.locgeneric import LocGeneric
import allure
from selenium.webdriver.support.select import Select

class WebGeneric(LocGeneric):
    def __init__(self, driver):
        LocGeneric.__init__(self, driver)
        global lc
        lc = LocGeneric(driver)

    def enter(self, locator_type, locator_val, input_val):
        e = self.locator(locator_type, locator_val)
        e.send_keys(input_val)

    def click(self, locator_type, locator_val):
        e = self.locator(locator_type, locator_val)
        e.click()

    def report_pass(self):
        pass

    def report_fail(self):
        pass

    def select_day(self, locator_type, locator_val, input_val):
        day = self.locator(locator_type, locator_val)
        select = Select(day)
        select.select_by_visible_text(input_val)

    def select_month(self, locator_type, locator_val, input_val):
        month = self.locator(locator_type, locator_val)
        select = Select(month)
        select.select_by_value(input_val)

    def select_year(self, locator_type, locator_val, input_val):
        year = self.locator(locator_type, locator_val)
        select = Select(year)
        select.select_by_index(input_val)

    def mouse_hr(self, locator_type, locator_val):
        ele= self.locator(locator_type, locator_val)
        webdriver.ActionChains(self.driver).move_to_element(ele).perform()