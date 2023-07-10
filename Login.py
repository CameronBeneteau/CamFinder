import time
from selenium import webdriver
from selenium.webdriver.common.by import By

import Const
import UserConfig.UserConfig as UserConfig


class Login:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def open_login_page(self):
        self.driver.get(Const.LOGIN_URL)

    def email_field_empty(self):
        return len(self.driver.find_elements(By.CLASS_NAME, "member__profile")) == 0

    def enter_email(self):
        self.driver.find_element(By.ID, Const.EMAIL_FIELD_ID).send_keys(
            UserConfig.EMAIL
        )

    def enter_password(self):
        self.driver.find_element(By.ID, Const.PASSWORD_FIELD_ID).send_keys(
            UserConfig.PASSWORD
        )

    def submit(self):
        buttons = self.driver.find_elements(By.TAG_NAME, "button")

        for button in buttons:
            if (
                Const.SIGN_IN_BUTTON_TEXT.lower().strip()
                in button.get_attribute("innerText").lower().strip()
            ):
                button.click()
                break

    # TODO: May need to refactor depending on security measures (phone, image, etc.)
    # <h1>Let's do a quick security check</h1>
    # https://www.linkedin.com/checkpoint/challenge/AgHypfhMZyfs1QAAAYkK52OLFYxGh0R3BHOrlpLUQzdqAbM9GI4Ztg3iWU7cNF6dsLvqeW-jZbTZKiuNqLHBIi1t8eZ4OQ?ut=1uiGC-jlmIjGQ1
    def wait_for_homepage(self):
        for _ in range(Const.MAX_HOMEPAGE_WAIT_TIME * 60):
            if self.driver.current_url == Const.HOMEPAGE_URL:
                return
            else:
                time.sleep(1)

        raise Exception(
            f"Could not load homepage within {Const.MAX_HOMEPAGE_WAIT_TIME} minutes."
        )

    def main(self):
        self.open_login_page()

        if self.driver.current_url == Const.LOGIN_URL:
            if self.email_field_empty():
                self.enter_email()
            self.enter_password()
            self.submit()

        self.wait_for_homepage()
