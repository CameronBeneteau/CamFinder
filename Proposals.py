import time
from selenium import webdriver
from selenium.webdriver.common.by import By

import Const
import UserConfig.UserConfig as UserConfig


class Proposals:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def open_request_page(self):
        self.driver.get(Const.REQUESTS_PAGE_URL)

    def check_for_new_proposal(self):
        proposalContainer = self.driver.find_elements(
            By.CSS_SELECTOR,
            "[data-test-service-marketplace-service-requests__list-container]",
        )

        if len(proposalContainer) != 0:
            return
        else:
            time.sleep(UserConfig.PROPOSAL_REFRESH_TIME * 60)
            self.main()

    def main(self):
        self.open_request_page()
        time.sleep(5)
        self.check_for_new_proposal()
