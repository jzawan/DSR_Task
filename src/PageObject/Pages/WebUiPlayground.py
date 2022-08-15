from src.PageObject.Locators.Locators import Locators_WebUiPlayground
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

base_url = "https://vladimirwork.github.io/web-ui-playground/"


class WebUiPlayground:

    def __init__(self, driver):
        self.driver = driver

    # Fields
    def get_first_name(self):
        return self.driver.find_element(By.NAME, Locators_WebUiPlayground.first_name)

    def get_last_name(self):
        return self.driver.find_element(By.NAME, Locators_WebUiPlayground.last_name)

    def get_email(self):
        return self.driver.find_element(By.NAME, Locators_WebUiPlayground.email)

    def get_phone_number(self):
        return self.driver.find_element(By.NAME, Locators_WebUiPlayground.phone_number)

    def get_male_gender_radio_button(self):
        return self.driver.find_element(By.XPATH, Locators_WebUiPlayground.male_gender_radio_button)

    def get_female_gender_radio_button(self):
        return self.driver.find_element(By.XPATH, Locators_WebUiPlayground.female_gender_radio_button)

    def get_i_agree(self):
        return self.driver.find_element(By.XPATH, Locators_WebUiPlayground.i_agree)

    def get_submit_button(self):
        return self.driver.find_element(By.NAME, Locators_WebUiPlayground.submit_button)

    # Validations
    def validate_fn_message(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(('xpath', Locators_WebUiPlayground.fname_validation)))
        return self.driver.find_element(By.XPATH, Locators_WebUiPlayground.fname_validation)

    def validate_ln_message(self):
        return self.driver.find_element(By.XPATH, Locators_WebUiPlayground.lname_validation)

    def validate_email_message(self):
        return self.driver.find_element(By.XPATH, Locators_WebUiPlayground.email_validation)

    def validate_phone_message(self):
        return self.driver.find_element(By.XPATH, Locators_WebUiPlayground.phone_validation)

    def validate_gender_message(self):
        return self.driver.find_element(By.XPATH, Locators_WebUiPlayground.gender_validation)

    def validate_i_agree_message(self):
        return self.driver.find_element(By.XPATH, Locators_WebUiPlayground.i_agree_validation)

    # Actions using in testcases

    def enter_first_name(self, firstname):
        self.get_first_name().send_keys(firstname)

    def enter_last_name(self, lastname):
        self.get_first_name().send_keys(lastname)

    def enter_email(self, emailid):
        self.get_first_name().send_keys(emailid)

    def enter_phone_number(self, phonenumber):
        self.get_first_name().send_keys(phonenumber)

    def fill_form(self, firstname, lastname, emailid, phonenumber):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(('name', Locators_WebUiPlayground.first_name)))
        self.get_first_name().send_keys(firstname)
        self.get_last_name().send_keys(lastname)
        self.get_email().send_keys(emailid)
        self.get_phone_number().send_keys(phonenumber)

    def click_male_gender_radio_button(self):
        # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(('xpath', self.use_this_address_button)))
        self.get_male_gender_radio_button().click()

    def click_i_agree(self):
        # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(('xpath', self.use_this_address_button)))
        self.get_i_agree().click()

    def click_submit_button(self):
        self.get_submit_button().click()

    def validate_alert_text(self):
        return self.driver.switch_to.alert.text

    def close_alert(self):
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        self.driver.switch_to.alert.dismiss()

    @staticmethod
    def get_base_url():
        return base_url
