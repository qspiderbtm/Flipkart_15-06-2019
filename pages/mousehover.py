import time
from pages.webgeneric import WebGeneric

class mouse_hover_page(WebGeneric):
    def __init__(self, driver):
        WebGeneric.__init__(self, driver)
        self.cls = '//*[@class="_2AkmmA _29YdH8"]'
        self.item = "Sneakers"
        self.hr = "//span[contains(text(),'Men')]"
        global wb
        wb = WebGeneric(driver)

    def cancel_popup(self):
        wb.click("xpath", self.cls)

    def mse_hr(self):
        wb.mouse_hr("xpath", self.hr)

    def clk_on_items(self):
        wb.click("xpath", self.item)
