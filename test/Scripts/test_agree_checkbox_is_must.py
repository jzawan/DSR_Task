from src.TestBase.WebDriverSetup import WebDriverSetup

from src.PageObject.Pages.WebUiPlayground import WebUiPlayground


class Test_DSR_Task(WebDriverSetup):

    def test_agree_checkbox_is_must(self):
        driver = self.driver
        web_ui_playground = WebUiPlayground(driver)
        self.driver.get(WebUiPlayground.get_base_url())
        web_ui_playground.fill_form("Jahanzaib", "Awan", "jahanzaibawan@testemail.com", "A")
        web_ui_playground.click_male_gender_radio_button()
        web_ui_playground.click_submit_button()
        web_ui_playground.validate_i_agree_message()
        assert "You must agree to the processing of personal data" in self.driver.page_source
