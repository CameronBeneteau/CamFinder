# import pprint

# from selenium import webdriver
# from selenium.webdriver.common.by import By

# import Info


# class Filter:
#     def __init__(self, driver: webdriver.Chrome):
#         self.driver = driver
#         self.serviceType = None
#         self.questionsToAnswers = None

#         self.setServiceType()
#         self.setQuestionsToAnswers()

#     def setServiceType(self):
#         self.serviceType = (
#             self.driver.find_element(
#                 By.CSS_SELECTOR, "[data-test-service-requests-detail__project-title]"
#             )
#             .get_attribute("innerText")
#             .split("\n")[0]
#         )

#     def getServiceType(self):
#         return self.serviceType

#     def setQuestionsToAnswers(self):
#         questions = self.driver.find_elements(
#             By.CSS_SELECTOR, "[data-test-service-requests-detail__description-question]"
#         )
#         answers = self.driver.find_elements(
#             By.CSS_SELECTOR, "[data-test-service-requests-detail__description-answer]"
#         )

#         self.questionsToAnswers = {}

#         for question, answer in zip(questions, answers):
#             questionText = question.get_attribute("innerText")
#             answerText = answer.get_attribute("innerText")

#             self.questionsToAnswers[questionText] = answerText

#         print(self.questionsToAnswers)

#     def getQuestionsToAnswers(self):
#         return self.questionsToAnswers

#     def getQuestionsText(self):
#         retList = []

#         questions = self.driver.find_elements(
#             By.CSS_SELECTOR, "[data-test-service-requests-detail__description-question]"
#         )

#         for question in questions:
#             retList.append(question.get_attribute("innerText"))

#         return retList

#     def getAnswersText(self):
#         retList = []

#         answers = self.driver.find_elements(
#             By.CSS_SELECTOR, "[data-test-service-requests-detail__description-answer]"
#         )

#         for answer in answers:
#             retList.append(answer.get_attribute("innerText"))

#         return retList

#     def getAllQuestionsAndAnswers(self):
#         print(self.getQuestionsText())
#         print(self.getAnswersText())

#     def filterOptions(self):
#         serviceType = self.getServiceType()

#         for question, options in Info.filter[serviceType.lower()].items():
#             answer = self.questionsToAnswers[question]
#             if not self.filterOption(question, options, answer):
#                 return False

#         return True

#     def filterOption(self, question, options, answer):
#         if options["type"] == "multiselect":
#             return self.filterMultiselectOption(question, options, answer)
#         elif options["type"] == "select":
#             return self.filterSelectOption(question, options, answer)
#         else:
#             return True

#     def filterMultiselectOption(self, question, options, answer, operator):
#         return True
#         # for value in options['']
#         # print("Filter multiselect option")
#         # return True

#     def filterSelectOption(self, question, options, answer):
#         print("Filter select option")
#         return options["filter"] in answer
