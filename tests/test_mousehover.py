# from pages.loginpage import LoginPage
# from pages.homepage import HomePage
import pytest

from pages.dropdown import drop_down_page
from pages.mousehover import mouse_hover_page

@pytest.mark.usefixtures("test_setup")
class TestMouseHover:
    def test_mouse_hr(self):
        driver = self.driver
        mhr = mouse_hover_page(driver)
        mhr.cancel_popup()
        mhr.mse_hr()
        # mhr.clk_on_items()
