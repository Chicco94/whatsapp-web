import time
import unittest
from unittest import TestCase

from selenium import webdriver

from simon import pages


class LoginBaseTestCase(TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.login_page = pages.LoginPage(self.driver)
        self.login_page.load()

    def tearDown(self):
        self.driver.close()


class LoginPageTests(LoginBaseTestCase):
    def test_can_open_whatsapp(self):
        self.assertTrue(self.login_page.is_title_matches())
        self.assertTrue(self.login_page.is_instruction_title_matches())

    def test_checkbox_remember_me_is_checked_by_default(self):
        self.assertTrue(self.login_page.is_remember_me_selected())

    def test_can_uncheck_checkbox_remember_me(self):
        self.login_page.remember_me = False
        self.assertFalse(self.login_page.is_remember_me_selected())

    def test_can_uncheck_and_check_again_checkbox_remember_me(self):
        self.login_page.remember_me = False
        self.assertFalse(self.login_page.is_remember_me_selected())
        self.login_page.remember_me = True
        self.assertTrue(self.login_page.is_remember_me_selected())

    def test_can_manually_login_successfully(self):
        base_page = pages.BasePage(self.driver)
        base_page.load()
        # time for you to read QR code and access whatsapp
        time.sleep(8)
        self.assertTrue(base_page.is_title_matches())
        self.assertTrue(base_page.is_welcome_page_available())
        self.assertTrue(base_page.is_nav_bar_page_available())
        self.assertTrue(base_page.is_search_page_available())
        self.assertTrue(base_page.is_pane_page_available())
        # chat is only available after you click on a person to open the chat
        self.assertFalse(base_page.is_chat_page_available())


if __name__ == "__main__":
    unittest.main()
