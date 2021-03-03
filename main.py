import os
from dotenv import load_dotenv
from selenium import webdriver, common
from selenium.webdriver.common.keys import Keys
from time import sleep

chrome_driver_path = "E:/Python/WebDriver/chromedriver.exe"
firefox_driver_path = "E:/Python/WebDriver/geckodriver.exe"
opera_driver_path = "E:/Python/WebDriver/operadriver.exe"


load_dotenv("E:/Python/EnvironmentVariables/.env")
USERNAME = os.getenv("Username_Instagram")
PASSWORD = os.getenv("Password_Instagram")

SIMILAR_ACCOUNT = "chefsteps"


class InstaFollower:
    def __init__(self, browser):
        b = browser.lower()
        if b == "chrome":
            self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        elif b == "firefox":
            self.driver = webdriver.Firefox(executable_path=firefox_driver_path)
        elif b == "opera":
            self.driver = webdriver.Opera(executable_path=opera_driver_path)
        else:
            print("Invalid browser")

    def find_element(self, xpath):
        while True:
            try:
                element = self.driver.find_element_by_xpath(xpath)
                return element
            except common.exceptions.ElementNotInteractableException:
                print("Element Not Interactable Exception")
                sleep(1)
            except common.exceptions.NoSuchElementException:
                print("No Such Element Exception")
                sleep(1)

    def login(self, url):
        self.driver.get(url)

        # Accept Cookies
        self.find_element(
            "/html/body/div[2]/div/div/div/div[2]/button[1]"
        ).click()

        # Input Username and Password and Log In
        self.find_element(
            '//*[@id="loginForm"]/div/div[1]/div/label/input'
        ).send_keys(
            USERNAME + Keys.TAB +
            PASSWORD + Keys.ENTER
        )

        # # Log In
        # self.find_element(
        #     '//*[@id="loginForm"]/div/div[3]/button'
        # ).click()

        # Don't save passwords
        self.find_element(
            '//*[@id="react-root"]/section/main/div/div/div/div/button'
        ).click()

        # Dismiss Notifications
        self.find_element(
            '/html/body/div[4]/div/div/div/div[3]/button[2]'
        ).click()

    def find_followers(self):
        pass

    def follow(self):
        pass


insta_follower = InstaFollower(browser="Chrome")
if insta_follower.driver is None:
    quit()
insta_follower.login(url="https://www.instagram.com/")
insta_follower.find_followers()
insta_follower.follow()

