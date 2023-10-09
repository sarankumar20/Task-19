# vist th url https://www.saucedemo.com/  and login with the following creditionals
# Username:standard_user
# password: standard_user
# try to fetch the following using python selenium
# 1.title
# 2.current url
# 3.extract whole content web page and save as file.txt format

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep

class Base:
    def __init__(self, link):
        # these are Instance attributes to base class
        self.url = link
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.Username = "standard_user"
        self.password = "standard_user"


    def validate_login_creditionals(self):
        #  to maximize browser  window and passing given url
        self.driver.maximize_window()
        # get() method to open url in browser
        self.driver.get(url)
        # sleep method used to wait browser for some seconds
        sleep(3)
        # we get Tag_id in web page and pass it has locators as value
        # And passing instance attributes (username and password) to send_keys as value
        self.driver.find_element(by=By.NAME, value="user-name").send_keys(self.Username)
        sleep(3)
        self.driver.find_element(by=By.NAME, value="password").send_keys(self.password)
        sleep(3)
        self.driver.find_element(by=By.ID, value="login-button").click()

    # to get title of web page
    def fetch_title(self):
        print(f'Title of the given URL is: {self.driver.title}')

    # to get current url of web-page
    def fetch_URL(self):
        current_url = self.driver.current_url
        print(f'web page of current_url is : {current_url}')
        if url == current_url:
            print("it match the  requirement")
        else:
            print("it not matched")

# we use Multiple inheritance to access parent class properties in child class
class Sub(Base):
    def txt_format(self):
        self.driver.get(url)
        text_file = self.driver.page_source
        file =open("Webpage_task_11.txt", 'w')
        file.write(text_file)
        file.close()
    def close(self):
        self.driver.get(url)
        self.driver.quit()

# object
url = "https://www.saucedemo.com/"

# Driver code
reference = Sub(url)
reference.validate_login_creditionals()
reference.fetch_title()
reference.fetch_URL()
reference.txt_format()
reference.close()


