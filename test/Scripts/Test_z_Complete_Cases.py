#
#
# from src.TestBase.WebDriverSetup import WebDriverSetup
#
# from src.PageObject.Pages.WebUiPlayground import WebUiPlayground
#
#
# class Test_DSR_Task(WebDriverSetup):
#
#     def test_fields_are_present_on_the_page(self):
#         driver = self.driver
#         self.driver.get(WebUiPlayground.get_base_url())
#         web_ui_playground = WebUiPlayground(driver)
#
#         web_ui_playground.get_first_name()
#         web_ui_playground.get_last_name()
#         web_ui_playground.get_email()
#         web_ui_playground.get_phone_number()
#         web_ui_playground.get_male_gender_radio_button()
#         web_ui_playground.get_female_gender_radio_button()
#         web_ui_playground.get_i_agree()
#         web_ui_playground.get_submit_button()
#
#     def test_complete_form(self):
#         driver = self.driver
#         self.driver.get(WebUiPlayground.get_base_url())
#         web_ui_playground = WebUiPlayground(driver)
#
#         web_ui_playground.fill_form("Jahanzaib", "Awan", "jahanzaibawan@testemail.com", "09876543210")
#         web_ui_playground.click_male_gender_radio_button()
#         web_ui_playground.click_i_agree()
#         web_ui_playground.click_submit_button()
#         web_ui_playground.close_alert()
#
#     def test_mandatory_fields(self):
#         driver = self.driver
#         web_ui_playground = WebUiPlayground(driver)
#         self.driver.get(WebUiPlayground.get_base_url())
#         web_ui_playground.click_submit_button()
#         web_ui_playground.validate_fn_message()
#         web_ui_playground.validate_ln_message()
#         web_ui_playground.validate_email_message()
#         web_ui_playground.validate_phone_message()
#         web_ui_playground.validate_gender_message()
#         web_ui_playground.validate_i_agree_message()
#
#     def test_invalid_first_name(self):
#         driver = self.driver
#         web_ui_playground = WebUiPlayground(driver)
#         self.driver.get(WebUiPlayground.get_base_url())
#         web_ui_playground.fill_form("1", "Awan", "jahanzaibawan@testemail.com", "09876543210")
#         web_ui_playground.click_male_gender_radio_button()
#         web_ui_playground.click_i_agree()
#         web_ui_playground.click_submit_button()
#         web_ui_playground.validate_fn_message()
#         assert "Valid first name is required" in self.driver.page_source
#
#
#     def test_invalid_last_name(self):
#         driver = self.driver
#         web_ui_playground = WebUiPlayground(driver)
#         self.driver.get(WebUiPlayground.get_base_url())
#         web_ui_playground.fill_form("Jahanzaib", "1", "jahanzaibawan@testemail.com", "09876543210")
#         web_ui_playground.click_male_gender_radio_button()
#         web_ui_playground.click_i_agree()
#         web_ui_playground.click_submit_button()
#         web_ui_playground.validate_ln_message()
#         assert "Valid last name is required" in self.driver.page_source
#
#     def test_invalid_email_address(self):
#         driver = self.driver
#         web_ui_playground = WebUiPlayground(driver)
#         self.driver.get(WebUiPlayground.get_base_url())
#         web_ui_playground.fill_form("Jahanzaib", "Awan", "1", "09876543210")
#         web_ui_playground.click_male_gender_radio_button()
#         web_ui_playground.click_i_agree()
#         web_ui_playground.click_submit_button()
#         web_ui_playground.validate_email_message()
#         assert "Valid email is required" in self.driver.page_source
#
#     def test_invalid_phone_number(self):
#         driver = self.driver
#         web_ui_playground = WebUiPlayground(driver)
#         self.driver.get(WebUiPlayground.get_base_url())
#         web_ui_playground.fill_form("Jahanzaib", "Awan", "jahanzaibawan@testemail.com", "A")
#         web_ui_playground.click_male_gender_radio_button()
#         web_ui_playground.click_i_agree()
#         web_ui_playground.click_submit_button()
#         web_ui_playground.validate_phone_message()
#         assert "Valid phone number is required" in self.driver.page_source
#
#     def test_choose_gender_radio_button_is_not_selected(self):
#         driver = self.driver
#         web_ui_playground = WebUiPlayground(driver)
#         self.driver.get(WebUiPlayground.get_base_url())
#         web_ui_playground.fill_form("Jahanzaib", "Awan", "jahanzaibawan@testemail.com", "A")
#         web_ui_playground.click_i_agree()
#         web_ui_playground.click_submit_button()
#         web_ui_playground.validate_gender_message()
#         assert "Choose your gender" in self.driver.page_source
#
#     def test_agree_checkbox_is_must(self):
#         driver = self.driver
#         web_ui_playground = WebUiPlayground(driver)
#         self.driver.get(WebUiPlayground.get_base_url())
#         web_ui_playground.fill_form("Jahanzaib", "Awan", "jahanzaibawan@testemail.com", "A")
#         web_ui_playground.click_male_gender_radio_button()
#         web_ui_playground.click_submit_button()
#         web_ui_playground.validate_i_agree_message()
#         assert "You must agree to the processing of personal data" in self.driver.page_source
