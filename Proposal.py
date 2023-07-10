import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

import Const
import UserConfig.UserConfig as UserConfig

# from Filter import Filter
from ProposalInfo import ProposalInfo

from DynamoDb.DynamoDb import DynamoDb
from Models.PofileInfo import ProfileInfo
from UserConfig.Script import Script
from Utils.DateTime import DateTime


class Proposal:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def open_latest_proposal(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "[data-test-service-request-details__accept]"
        ).click()

    def enter_proposal_script(self):
        self.driver.find_element(By.TAG_NAME, "textarea").send_keys(
            Script().getScript()
        )

    def check_consultation(self):
        if UserConfig.FREE_CONSULTATION:
            self.driver.find_element(
                By.CSS_SELECTOR, "[data-test-text-selectable-option__label]"
            ).click()

    def submit(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "[data-test-proposal-submission-modal__submit-button]"
        ).click()

    def save_profil_details(self):
        proposalInfo = ProposalInfo(self.driver)

        info: ProfileInfo = proposalInfo.get_proposal_info()

        # Pass same time to both updates?
        self.save_to_text_file(info)
        self.save_to_database(info)

    def save_to_database(self, info: ProfileInfo):
        dynamoDb = DynamoDb(UserConfig.USER_ID, Const.TABLE_NAME, UserConfig.REGION)
        dynamoDb.putItem(info)

    def save_to_text_file(self, info: ProfileInfo):
        with open("sent_proposals.csv", "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(
                [
                    UserConfig.USER_ID,
                    DateTime().get_time_formatted(),
                    info.name,
                    info.service_type,
                    info.location,
                    info.profile_description,
                    info.profile_link,
                ]
            )

    def main(self):
        self.open_latest_proposal()
        time.sleep(5)
        self.enter_proposal_script()
        self.check_consultation()
        self.submit()
        self.save_profil_details()