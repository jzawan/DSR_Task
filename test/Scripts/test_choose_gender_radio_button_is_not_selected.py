from src.TestBase.WebDriverSetup import WebDriverSetup

from src.PageObject.Pages.WebUiPlayground import WebUiPlayground


class Test_DSR_Task(WebDriverSetup):

    def test_choose_gender_radio_button_is_not_selected(self):
        driver = self.driver
        web_ui_playground = WebUiPlayground(driver)
        self.driver.get(WebUiPlayground.get_base_url())
        web_ui_playground.fill_form("Jahanzaib", "Awan", "jahanzaibawan@testemail.com", "A")
        web_ui_playground.click_i_agree()
        web_ui_playground.click_submit_button()
        web_ui_playground.validate_gender_message()
        assert "Choose your gender" in self.driver.page_source
