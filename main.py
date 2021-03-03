import os
from dotenv import load_dotenv
from selenium import webdriver, common
from selenium.webdriver.common.keys import Keys
from time import sleep
import math

chrome_driver_path = "E:/Python/WebDriver/chromedriver.exe"
firefox_driver_path = "E:/Python/WebDriver/geckodriver.exe"
opera_driver_path = "E:/Python/WebDriver/operadriver.exe"


load_dotenv("E:/Python/EnvironmentVariables/.env")
USERNAME = os.getenv("Username_Instagram")
PASSWORD = os.getenv("Password_Instagram")

BASE_URL = "https://www.instagram.com/"
SIMILAR_ACCOUNT = "craigpython"  # "chefsteps"


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
            except common.exceptions.NoSuchElementException:
                print("No Such Element Exception")
            finally:
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

    def find_followers(self, url):
        self.driver.get(url)

        # Followers Pop-up
        self.find_element(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a'
        ).click()

        # Expand Followers
        """
        In this case we're executing some Javascript using execute_script() method.
        The method can accept the script as well as a HTML element.
        The modal in this case, becomes the arguments[0] in the script.
        Then we're using Javascript to say:
            "scroll the top of the popup element by the height of the popup"
            
        NOTE that .scrollTop and .scrollHeight are DOM Element Properties e.g. HTML Elements,
            not Python WebDriver / WebElement properties.
            See https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollTop
        """
        # followers = self.find_element('/html/body/div[5]/div/div/div[2]')
        #
        # # JavaScript solution
        # #   Get the first approx 80 followers (scroll the popup down 10 times)
        # #   The pop-up displays about 8 followers in view
        # for _ in range(10):
        #     self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers)
        #     sleep(2)  # Allow the list to update

        # Python / Selenium solution
        #   Get the first 132 followers (scroll the popup down 10 times)
        for _ in range(10):
            self.find_element('/html/body/div[5]/div/div/div[2]//a').send_keys(Keys.END)
            sleep(2)  # Allow the list to update

    def follow(self):
        pass


insta_follower = InstaFollower(browser="Chrome")
if insta_follower.driver is None:
    quit()
insta_follower.login(url=BASE_URL)
insta_follower.find_followers(url=BASE_URL + SIMILAR_ACCOUNT)
insta_follower.follow()

