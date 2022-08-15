from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

base_url = "https://vladimirwork.github.io/web-ui-playground/"


class Locators_WebUiPlayground:
    # Fields locators
    first_name = "FirstName"
    last_name = "LastName"
    email = "Email"
    phone_number = "PhoneNumber"
    male_gender_radio_button = "//input[@value='Male']"
    female_gender_radio_button = "//input[@value='Female']"
    i_agree = "//input[@name='Agreement']"
    submit_button = "submitbutton"

    # Validation Messages Locators
    fname_validation = "//p[contains(text(),'Valid first name is required.')]"
    lname_validation = "//p[contains(text(),'Valid last name is required.')]"
    email_validation = "//p[contains(text(),'Valid email is required.')]"
    phone_validation = "//p[contains(text(),'Valid phone number is required.')]"
    gender_validation = "//p[contains(text(),'Choose your gender.')]"
    i_agree_validation = "//p[contains(text(),'You must agree to the processing of personal data.')]"
