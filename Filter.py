from selenium import webdriver
from selenium.webdriver.common.by import By

import UserConfig.UserConfig as UserConfig

from Enums.QuestionEnum import QuestionEnum
from Models.Question import Question


class Filter:
    questions_to_answers: dict[str, str] = {}
    service_type: str = ""

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.service_type = self.get_service_type()
        self.questions_to_answers = self.get_questions_and_answers()

    def get_service_type(self) -> str:
        return (
            self.driver.find_element(
                By.CSS_SELECTOR, "[data-test-service-requests-detail__project-title]"
            ).get_attribute("innerText")
        ).split("\n")[0]

    def get_questions_and_answers(self):
        questions = self.driver.find_elements(
            By.CSS_SELECTOR, "[data-test-service-requests-detail__description-question]"
        )
        answers = self.driver.find_elements(
            By.CSS_SELECTOR, "[data-test-service-requests-detail__description-answer]"
        )

        ret_dict = {}

        for question, answer in zip(questions, answers):
            question_text = question.get_attribute("innerText")
            answer_text = answer.get_attribute("innerText")

            ret_dict[question_text] = answer_text

        return ret_dict

    def filter_questions(self) -> str:
        for question_key, question_value in UserConfig.FILTERS.get(
            self.service_type, {}
        ).items():
            question_result = self.filter_question(
                question_key, question_value, self.questions_to_answers[question_key]
            )

            if question_result:
                return question_result

        return ""

    def filter_question(
        self, question_key: str, question_value: Question, answer: str
    ) -> str:
        if question_value.category == QuestionEnum.SELECT:
            return self.filter_select_question(question_key, question_value, answer)
        elif question_value.category == QuestionEnum.MULTISELECT:
            return self.filter_multiselect_question(
                question_key, question_value, answer
            )
        else:
            return ""

    def filter_select_question(
        self, question_key: str, question_value: Question, answer: str
    ) -> str:
        for option in question_value.exclude:
            if option.lower() in answer.lower():
                return f"Filter option: '{option}' found in select question: '{question_key}'"

        return ""

    def filter_multiselect_question(
        self, question_key: str, question_value: Question, answer: str
    ) -> str:
        for option in question_value.exclude:
            if option.lower() in answer.lower():
                return f"Filter option: '{option}' found in multiselect question '{question_key}'"

        return ""
