import configparser
from selenium.webdriver.common.by import By

from util.DelayUtil import WaitWrapper
import os

class LoginByPassword:
    def __init__(self, driver):
        self.driver = driver
        self.wait_wrapper = WaitWrapper(driver)
        self.config = configparser.ConfigParser()
        self.config.read(os.path.join(os.path.dirname(__file__), './config.ini'))

    def login(self):
        # 登录
        user_password_button = self.wait_wrapper((By.CSS_SELECTOR, '[data-cypress="sign-in-with-password"]'))
        user_password_button.click()

        user_id = self.wait_wrapper((By.CSS_SELECTOR, '[name=login]'))
        # user_id = driver.find_element(By.CSS_SELECTOR, '[name=login]')
        # user_password = wait_wrapper((By.CSS_SELECTOR, '[name="password"]'))
        user_password = self.driver.find_element(By.CSS_SELECTOR, '[name="password"]')
        user_id.send_keys(self.config['DEFAULT']['userId'])
        user_password.send_keys(self.config['DEFAULT']['userPassword'])
        confirm_button = self.driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
        confirm_button.click()

class LoginByQQ:
    def __init__(self, driver):
        self.driver = driver
        self.wait_wrapper = WaitWrapper(driver)
        self.config = configparser.ConfigParser()
        self.config.read(os.path.join(os.path.dirname(__file__), './config.ini'))

    def login(self):
        # 登录
        qq_login_button = self.wait_wrapper((By.CSS_SELECTOR, '[title="QQ"]'))
        qq_login_button.click()

        password_login_button = self.wait_wrapper((By.CSS_SELECTOR, '#switcher_plogin'))
        password_login_button.click()

        qq_id = self.wait_wrapper((By.CSS_SELECTOR, '.inputOuter')).find_element(By.CSS_SELECTOR, 'input')
        qq_id.clear()
        qq_id.send_keys(self.config['DEFAULT']['qqid'])

        qq_password = self.wait_wrapper((By.CSS_SELECTOR, '[type="password"]'))
        qq_password.send_keys(self.config['DEFAULT']['qqPassword'])

        submitButton = self.driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
        submitButton.click()