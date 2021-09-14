import unittest
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options



class BuymeObjects:
    driver = None

    def __init__(self, browser):
        self.chrome_options = Options()
        self.edge_options = Options()
        self.driver = None
        self.action_chains = None
        self.first_enrollment_button = None
        self.second_enrollment_button = None
        self.first_name_button = None
        self.mail_button = None
        self.password_button = None
        self.confirm_password_button = None
        self.final_enrollment_button = None
        self.browser = browser
        self.open_page()
        self.set_elements()

    def get_browser(self):
        return "chrome"

    def open_page(self):
        self.set_driver()
        self.driver.get("https://buyme.co.il/")

    def set_option(self):
        self.chrome_options.add_argument("--disable-extensions")
        self.chrome_options.add_argument("--incognito")
        self.chrome_options.add_argument("--disable-popup-blocking")
        self.chrome_options.add_argument("--start-maximized")
        self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument("--no-sandbox")

    def set_driver(self):
        if self.browser == "chrome":
            self.set_option()
            self.driver = webdriver.Chrome(options=self.chrome_options)
        else:
            self.driver = webdriver.Edge()

    def set_elements(self):
        self.first_enrollment_button = self.driver.find_element_by_xpath(
            '//*[@id="ember957"]/div/ul[1]/li[3]/a/span[2]').click()
        self.driver.implicitly_wait(10)
        self.second_enrollment_button = self.driver.find_element_by_xpath(
            '//*[@id="ember924"]/div/div[1]/div/div/div[3]/div[1]/span').click()
        self.driver.implicitly_wait(10)
        # self.first_name_button = self.driver.find_element_by_('//*[@id="ember1747"]')
        self.first_name_button = self.driver.find_element_by_css_selector("input[placeholder = 'שם פרטי']")
        self.mail_button = self.driver.find_element_by_css_selector("input[placeholder = 'מייל']")
        self.password_button = self.driver.find_element_by_css_selector("input[placeholder = 'סיסמה']")
        self.confirm_password_button = self.driver.find_element_by_css_selector("input[placeholder = 'אימות סיסמה']")
        self.final_enrollment_button = self.driver.find_element_by_css_selector("button[gtm = 'הרשמה ל-BUYME']")

    def write_first_name(self, first_name):
        self.first_name_button.send_keys(first_name)

    def write_mail(self, mail):
        self.mail_button.send_keys(mail)

    def write_password(self, password):
        self.password_button.send_keys(password)
        self.confirm_password_button.send_keys(password)

    def final_enrolment(self):
        self.final_enrollment_button.submit()
        time.sleep(1)

    def get_title(self):
        return self.driver.title

    def close_driver(self):
        self.driver.close()

    def check_enrolment(self):
        try:
            self.driver.find_element_by_id('ember1530')
            return True
        except:
            return False
