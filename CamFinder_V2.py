# CamFinder - Linked Auto Profinder
# Version 2
#
# By: Cameron Beneteau
# Date: July 9th, 2023

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Login import Login
from Proposal import Proposal
from Proposals import Proposals

options = Options()
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options)

if __name__ == "__main__":
    print("-" * 25 + " Welcome to CamFinder V2 " + "-" * 25)
    print("-" * 75)

    while True:
        try:
            login = Login(driver)
            login.main()

            while True:
                print("\nOpening new requests page...\n")
                print("-" * 75)

                proposals = Proposals(driver)
                proposals.main()

                proposal = Proposal(driver)
                proposal.main()

        except Exception as e:
            print("Error Detected - Restarting CamFinder V2 Now")
            print(e)
