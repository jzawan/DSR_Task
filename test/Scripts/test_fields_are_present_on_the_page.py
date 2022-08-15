import pytest

from src.TestBase.WebDriverSetup import WebDriverSetup

from src.PageObject.Pages.WebUiPlayground import WebUiPlayground


class Test_DSR_Task(WebDriverSetup):

    def test_fields_are_present_on_the_page(self):
        driver = self.driver
        self.driver.get(WebUiPlayground.get_base_url())
        web_ui_playground = WebUiPlayground(driver)

        web_ui_playground.get_first_name()
        web_ui_playground.get_last_name()
        web_ui_playground.get_email()
        web_ui_playground.get_phone_number()
        web_ui_playground.get_male_gender_radio_button()
        web_ui_playground.get_female_gender_radio_button()
        web_ui_playground.get_i_agree()
        web_ui_playground.get_submit_button()