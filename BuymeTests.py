import random
import unittest
from BuymeObjects import BuymeObjects
from lxml import etree as Et
from random import randint

TAGS = ["browser_type", "excepted_title", "first_name", "mail", "password", "password_confirm"]


class MyTestCase(unittest.TestCase):
    browser = None
    first_name = None
    mail = None
    password = None
    root = None
    title = None
    my_object = None

    @classmethod
    def setUpClass(cls):
        cls.root = Et.parse('config_buy_me_ex').getroot()
        cls.browser = cls.root.find("browser").text
        cls.first_name = cls.root.find("first_name").text

        cls.mail = cls.root.find("mail").text
        cls.password = cls.root.find("password").text
        cls.title = cls.root.find("title").text
        cls.my_object = BuymeObjects(cls.browser)

    def test_enrolment(self):
        num = randint(0, 10000)
        self.my_object.write_first_name(self.first_name)
        self.my_object.write_mail(str(num)+self.mail)
        self.my_object.write_password(self.password)
        self.my_object.final_enrolment()
        enrolment_successes = self.my_object.check_enrolment()
        self.assertTrue(enrolment_successes, "enrolment failed")

    def test_title(self):
        self.assertEqual(self.my_object.get_title(), self.title, "wrong title")

    @classmethod
    def tearDownClass(cls):
        cls.my_object.close_driver()

if __name__ == '__main__':
   log_file = 'log_file.txt'
   with open(log_file, "w") as f:
       runner = unittest.TextTestRunner(f)
       unittest.main(testRunner=runner)
