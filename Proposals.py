import time
from selenium import webdriver
from selenium.webdriver.common.by import By

import Const
import UserConfig.UserConfig as UserConfig

from Utils.DateTime import DateTime


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
            print("Proposal found - opening proposal submission window\n")
            return
        else:
            print("No proposals found\n")
            print(f"Refreshing page in {UserConfig.PROPOSAL_REFRESH_TIME} minutes")
            time.sleep(UserConfig.PROPOSAL_REFRESH_TIME * 60)
            print("-" * 75)
            print(f"Refreshed page on {DateTime().get_time_formatted()}\n")
            self.main()

    def main(self):
        self.open_request_page()
        time.sleep(5)
        self.check_for_new_proposal()
