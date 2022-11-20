# CamFinder - Linked AutoProfinder
# Version 1
# 
# By: Cameron Beneteau
# Date: November 19th, 2022

#  Includes:

# Next Steps:


# Imports
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

# Selenium/ChromeDriver Setup

current_url = ""    
login_link = "https://www.linkedin.com/login"
homepage_link = "https://www.linkedin.com/feed/"
old_client_requests_link = "https://www.linkedin.com/profinder/requests?trk=services_seo_home_client_requests"
client_requests_link = "https://www.linkedin.com/service-marketplace/provider/requests/?trk=services_seo_home_client_requests"
incorrect_url = 'https://www.linkedin.com/services?trk=d_flagship3_nav&'

refresh_time = 10 # Minutes

# options = Options()
# options.add_argument(r"--user-data-dir=C:\Users\camer\AppDtata\Local\Google\Chrome\User Data") #e.g. C:\Users\You\AppData\Local\Google\Chrome\User Data
# options.add_argument(r'--profile-directory=Profile 6') #e.g. Profile 3
# driver = webdriver.Chrome(executable_path=r'C:\Users\camer\Desktop\Linkedin Cam Finder\chromedriver.exe', options=options)
# driver.get(login_link)

import Info
import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import csv

options = Options()

# options.add_argument("user-data-dir=C:\\Users\\camer\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 6")
options.add_argument("user-data-dir=C:\\Users\\Administrator\\AppData\Local\\Google\Chrome\\User Data\\Profile 2")

options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation"])

# driver = webdriver.Chrome(executable_path=r'C:\Users\camer\Desktop\Linkedin Cam Finder\chromedriver.exe', options=options)
driver = webdriver.Chrome(executable_path=r'C:\Users\Administrator\Desktop\Cameron\CamFinder\chromedriver.exe', options=options)

# Load Login Page & Attempt to Login

def login():
    print("Attempting To Login...\n")
    try:
        driver.get(login_link)
        if driver.current_url == login_link:
            try:
                email_field = driver.find_element_by_id("username")
                #print(email_field)
                email_field.send_keys(Info.email)
                print("Email Entered")
                # time.sleep(1)
                password_field = driver.find_element_by_id("password")
                #print(password_field)
                password_field.send_keys(Info.password)
                print("Password Entered")
                # time.sleep(1)
                # sign_in_but = driver.find_element_by_id("")
                password_field.send_keys(Keys.RETURN)
                print("Sign In Clicked\n")
            except:
                print('Email and/or Password field not found, please enter the missing information and press "Sign in".\n')
                pass
        elif driver.current_url == homepage_link:
            print("Login Info Saved - Loading Homepage...\n")
    except:
        print("Error - Please Restart The Program")

def homepage_loaded() -> bool:
    if driver.current_url == homepage_link:
        print("Homepage Loaded\n")
        time.sleep(1)
        return True
    else:
        print("Homepage Not Loaded")
        return False

def client_requests_page():
    driver.get(client_requests_link)
    print("Opening Client Requests Page...\n")
    print("-" * 75)

def check_for_proposals():
    
    while True:

        name = "Test - name"
        desc = "Test - desc"
        break_loop = False
        time.sleep(5)

        submit_proposal_button = driver.find_elements_by_class_name('service-marketplace-provider-service-requests-detail__metadata-action')
        # submit_proposal_button = []

        if len(submit_proposal_button) > 0:
            for element in submit_proposal_button:
                if "Submit proposal" in element.get_attribute("innerText"):
                    name = driver.find_elements_by_class_name("artdeco-entity-lockup__title")[-1].get_attribute("innerText").split("\n")[0]
                    desc = driver.find_elements_by_class_name("artdeco-entity-lockup__subtitle")[-1].get_attribute("innerText").split("\n")[0]
                    element.click()
                    print("Proposal Found - Opening Proposal Submission Page...\n")
                    print(f"Name: {name}")
                    print(f"Description: {desc}")
                    print()
                    time.sleep(5)
                    break_loop = True
                    break
        else:           
            print("No Proposals Found\n")
            print("Refreshing Page in", str(refresh_time), "Minutes", sep = " ")
            print("-" * 75)
            time.sleep(refresh_time * 60)
            driver.get(client_requests_link)
            now = datetime.now()
            time_string = now.strftime("%b/%d/%Y @ %I:%M %p")
            print("Refreshed Page on", time_string, "\n", sep = " ")

        if break_loop:
                break

    proposal_text_field = driver.find_elements_by_css_selector("[id*=PROPOSAL-DETAILS]")
    # proposal_text_field = driver.find_element_by_id('multiline-text-form-component-marketplaceProposalSubmissionFormElementV2-PROPOSAL-DETAILS-marketplaceProject-15198997818-SERVICE-MARKETPLACE')
    proposal_text_field[0].send_keys(Info.message)
    print("Custom Message Entered\n")
    # time.sleep(5)

    # CLICK NOT WORKING #
    # if Info.free_consultation:
    #     phone_consultation_check = driver.find_element_by_class_name("fb-form-element__checkbox")
    #     print("Phone Consultation Option Checked\n")
    #     phone_consultation_check.click()
    # else:
    #     print("Phone Consultation Option Left Unchecked\n")
    ####################

    # time.sleep(5)

    continue_proposal_button = driver.find_elements(By.CSS_SELECTOR, '.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view')
    # send_proposal_button = driver.find_elements_by_class_name('artdeco-button--primary')
    
    for element in (continue_proposal_button):
        if "Continue" == element.get_attribute("innerText"):
            element.click()

    send_proposal_button = driver.find_elements(By.CSS_SELECTOR, '.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view')

    for element in (send_proposal_button):
        if "Submit" == element.get_attribute("innerText"):
            element.click()

            now = datetime.now()
            date_csv_str = now.strftime("%Y-%m-%d")
            time_csv_str = now.strftime("%H:%M:%S")

            with open("sent_proposals.csv", "a", newline='') as file:
                writer = csv.writer(file)
                writer.writerow([date_csv_str, time_csv_str, name, desc]) # write a row to the csv file
            
            print("Proposal Submitted & Recorded to CSV File\n")
            time.sleep(5)
            driver.get(client_requests_link)
            time_string = now.strftime("%b/%d/%Y @ %I:%M %p")
            print("Refreshed Page on", time_string, "\n", sep = " ")
            break

    print("-" * 75)

def close_messages():

    close_message_button = driver.find_elements_by_xpath("//*[@class='msg-overlay-bubble-header__control' and @class='artdeco-button artdeco-button--circle' and @class='artdeco-button--muted' and @class='artdeco-button--1' and @class='artdeco-button--tertiary' and @class='ember-view']")
    print(close_message_button)
    for b in close_message_button:
        b.click()

def main():

    login()
    
    while not homepage_loaded():
        pass
    
    client_requests_page()

    while True:
        #close_messages()
        check_for_proposals()

if __name__ == "__main__":

    print("-" * 25 + " Welcome to CamFinder V1 " + "-" * 25)
    print("-" * 75)

    while True:
        try:
            main()
        except Exception as e:
            print("-" * 75)
            print("Error Detected - Restarting CamFinder Now")
            print(e)
            print("-" * 75)
