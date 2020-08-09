"""
    File Name       :   instagram.py
    Project         :   planckbot
    Package         :   instantig
    Created On      :   AUG 09 2020
    Last Modified   :   AUG 9 2020
    Author          :   Planck Code <planckcode@gmail.com>
    Developer       :   Planck Studio
    Url             :   https://github.com/planckc0de/planckbot
"""
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


class Instagram(object):
    def __init__(self, username, password):
        self.chrome_driver_path = "Enter your path"
        self.browser_profile = webdriver.ChromeOptions()
        self.browser_profile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        self.browser = webdriver.Chrome(self.chrome_driver_path, chrome_options=self.browser_profile)
        self.username = username
        self.password = password

        # Default wait time
        self.rest = 3

    # Instagram login
    def login(self):
        self.browser.get('https://www.instagram.com/accounts/login/')
        time.sleep(self.rest)
        # Get input element
        username_input = self.browser.find_elements_by_css_selector('form input')[0]
        password_input = self.browser.find_elements_by_css_selector('form input')[1]

        # Set input element
        username_input.send_keys(self.username)
        password_input.send_keys(self.password)

        # Hit login button
        password_input.send_keys(Keys.ENTER)
        print('Login successfully')

    # Close notification dialog
    def close_notification_dialog(self):
        time.sleep(self.rest)
        try:
            self.browser.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()
        except NoSuchElementException:
            print('Element not found')

    # Follow user with username
    def follow_user(self, username):
        try:
            self.browser.get('https://www.instagram.com/' + username + '/')
            time.sleep(self.rest)
            button = self.browser.find_elements_by_css_selector('button')
            follow = button[0]
            if follow.text != 'Following':
                if follow.text != 'Requested':
                    follow.click()
                    print('User followed or requested')
                else:
                    print('Already requested')
            else:
                print('Already following')
        except NoSuchElementException:
            print('Element not found')

    # Unfollow user with username
    def unfollow_user(self, username):
        try:
            self.browser.get('https://www.instagram.com/' + username + '/')
            time.sleep(self.rest)
            button = self.browser.find_elements_by_css_selector('button')
            unfollow = button[1]
            unfollow.click()
            self.browser.find_element_by_css_selector('.-Cab_').click()
            print('User unfollowed')
        except NoSuchElementException:
            print('Element not found')

    # Follow multiple users
    def multiple_follow(self, username_list):
        for username in username_list:
            self.follow_user(username)
        print("Multiple Follow completed")

    # Unfollow multiple users
    def multiple_unfollow(self, username_list):
        for username in username_list:
            self.unfollow_user(username)
        print("Multiple Unfollow completed")

    # Close browser it self
    def close_browser(self):
        print('Session end')
        self.browser.quit()

    # Terminate process
    def __exit__(self, exc_type, exc_value, traceback):
        self.close_browser()
