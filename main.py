import os
from dotenv import load_dotenv
from selenium import webdriver

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
            driver = webdriver.Chrome(executable_path=chrome_driver_path)
        elif b == "firefox":
            driver = webdriver.Firefox(executable_path=firefox_driver_path)
        elif b == "opera":
            driver = webdriver.Opera(executable_path=opera_driver_path)
        else:
            print("Invalid browser")

    def login(self):
        login_page = "https://www.instagram.com/"
        pass

    def find_followers(self):
        pass

    def follow(self):
        pass


insta_follower = InstaFollower("Chrome")
insta_follower.login()
insta_follower.find_followers()
insta_follower.follow()

