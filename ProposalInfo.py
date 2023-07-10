from selenium import webdriver
from selenium.webdriver.common.by import By

from Models.PofileInfo import ProfileInfo


class ProposalInfo:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def get_proposal_info(self) -> ProfileInfo:
        return ProfileInfo(
            self.get_name(),
            self.get_service_type(),
            self.get_location(),
            self.get_profile_description(),
            self.get_profile_link(),
        )

    def get_name(self) -> str:
        return (
            self.driver.find_element(
                By.CSS_SELECTOR,
                "[data-test-service-requests-detail__creator-title]",
            )
            .get_attribute("innerText")
            .split("\n")[0]
        )

    def get_service_type(self) -> str:
        return (
            self.driver.find_element(
                By.CSS_SELECTOR, "[data-test-service-requests-detail__project-title]"
            ).get_attribute("innerText")
        ).split("\n")[0]

    def get_location(self) -> str:
        return self.driver.find_element(
            By.CSS_SELECTOR, "[data-test-service-requests-detail__location]"
        ).get_attribute("innerText")

    def get_profile_description(self) -> str:
        return (
            self.driver.find_element(
                By.CSS_SELECTOR, "[data-test-service-requests-detail__creator-subtitle]"
            )
            .get_attribute("innerText")
            .split("\n")[0]
        )

    def get_profile_link(self) -> str:
        return self.driver.find_element(
            By.CSS_SELECTOR, "[data-test-service-requests-detail__creator-title-link]"
        ).get_attribute("href")
