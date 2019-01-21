import os
from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.common.exceptions import NoSuchElementException

GOOGLE_CHROME_BIN = "/usr/bin/google-chrome"
CHROMEDRIVER_PATH = "/usr/bin/chromedriver"
SCROLL_PAUSE_TIME = 0.25


class FacebookLogin:

    def __init__(self):
        chrome_bin = os.environ.get(GOOGLE_CHROME_BIN)
        options = webdriver.ChromeOptions()
        options.binary_location = chrome_bin
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('headless')
        options.add_argument('--disable-notifications')
        options.add_argument('--disable-infobars')
        options.add_argument('window-size=1200x600')
        self.driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=options)
        self.url = 'https://facebook.com/login'

    def start_crawler(self):
        print("\nStarting Scraping...\n")
        self.driver.get(self.url)

    def facebook_login(self, get_user, get_pwd):
        user_id = self.driver.find_element_by_id('email')
        user_id.send_keys(get_user)

        password = self.driver.find_element_by_id('pass')
        password.send_keys(get_pwd)

        self.driver.find_element_by_xpath("//*[@type='submit']").click()
        return self.driver

    def scroll(self):
        while True:
            try:
                self.driver.find_element_by_class_name('_4khu')
                print('Reached end!')
                break
            except ValueError:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(SCROLL_PAUSE_TIME)

    def close_connection(self):
        self.driver.quit()
