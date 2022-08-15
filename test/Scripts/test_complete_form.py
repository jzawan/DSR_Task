from selenium import webdriver
from src.TestBase.WebDriverSetup import WebDriverSetup

from src.PageObject.Pages.WebUiPlayground import WebUiPlayground


class Test_DSR_Task(WebDriverSetup):

    def test_complete_form(self):
        driver = self.driver
        self.driver.get(WebUiPlayground.get_base_url())
        web_ui_playground = WebUiPlayground(driver)

        web_ui_playground.fill_form("Jahanzaib", "Awan", "jahanzaibawan@testemail.com", "09876543210")
        web_ui_playground.click_male_gender_radio_button()
        web_ui_playground.click_i_agree()
        web_ui_playground.click_submit_button()
        assert '{"FirstName":"Jahanzaib","LastName":"Awan","Email":"jahanzaibawan@testemail.com",' \
               '"PhoneNumber":"09876543210","Gender":"Male","Agreement":true}' in \
               web_ui_playground.validate_alert_text()
        web_ui_playground.close_alert()
