from src.TestBase.WebDriverSetup import WebDriverSetup

from src.PageObject.Pages.WebUiPlayground import WebUiPlayground


class Test_DSR_Task(WebDriverSetup):

    def test_invalid_first_name(self):
        driver = self.driver
        web_ui_playground = WebUiPlayground(driver)
        self.driver.get(WebUiPlayground.get_base_url())
        web_ui_playground.fill_form("1", "Awan", "jahanzaibawan@testemail.com", "09876543210")
        web_ui_playground.click_male_gender_radio_button()
        web_ui_playground.click_i_agree()
        web_ui_playground.click_submit_button()
        web_ui_playground.validate_fn_message()
        assert "Valid first name is required" in self.driver.page_source