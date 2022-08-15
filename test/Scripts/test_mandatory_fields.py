from src.TestBase.WebDriverSetup import WebDriverSetup

from src.PageObject.Pages.WebUiPlayground import WebUiPlayground


class Test_DSR_Task(WebDriverSetup):

    def test_mandatory_fields(self):
        driver = self.driver
        web_ui_playground = WebUiPlayground(driver)
        self.driver.get(WebUiPlayground.get_base_url())
        web_ui_playground.click_submit_button()
        web_ui_playground.validate_fn_message()
        web_ui_playground.validate_ln_message()
        web_ui_playground.validate_email_message()
        web_ui_playground.validate_phone_message()
        web_ui_playground.validate_gender_message()
        web_ui_playground.validate_i_agree_message()