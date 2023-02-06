import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Constants for the promised download and upload speed
PROMISED_DOWN = 50
PROMISED_UP = 10


class InternetSpeedTwitterBot:
    def __init__(self):
        # Get the path to the ChromeDriver from the environment variables
        self.chrome_driver_path = os.getenv("path")

        # Initialize the ChromeDriver service
        self.service = Service(self.chrome_driver_path)

        # Start a ChromeDriver session
        self.driver = webdriver.Chrome(service=self.service)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        def get_internet_speed(self):
            """
            Get the current internet speed
            """
            # Navigate to speedtest.net
            self.driver.get(url="https://speedtest.net")

            # Wait for page to load
            time.sleep(3)

            # Click the "Go" button to start the speed test
            go_btn = self.driver.find_element(By.CSS_SELECTOR,
                                              "#container > div > div.main-content > div > div > div > "
                                              "div.pure-u-custom-speedtest > "
                                              "div.speedtest-container.main-row > div.start-button > a > "
                                              "span.start-text")
            go_btn.click()

            # Wait for speed test to complete
            time.sleep(60)

            # Get the download speed
            self.down = self.driver.find_element(By.CSS_SELECTOR,
                                                 '#container > div > div.main-content > div > div > div '
                                                 '> div.pure-u-custom-speedtest > '
                                                 'div.speedtest-container.main-row > div.main-view > div '
                                                 '> div.result-area.result-area-test > div > div > '
                                                 'div.result-container-speed.result-container-speed'
                                                 '-active > div.result-container-data > '
                                                 'div.result-item-container.result-item-container-align'
                                                 '-center > div > div.result-data.u-align-left > span').text

            # Get the upload speed
            self.up = self.driver.find_element(By.CSS_SELECTOR, '#container > div > div.main-content > div > div > '
                                                                'div > '
                                                                'div.pure-u-custom-speedtest > '
                                                                'div.speedtest-container.main-row > div.main-view > '
                                                                'div > '
                                                                'div.result-area.result-area-test > div > div > '
                                                                'div.result-container-speed.result-container-speed'
                                                                '-active '
                                                                '> div.result-container-data > '
                                                                'div.result-item-container.result-item-container-align'
                                                                '-left > div > div.result-data.u-align-left > span').text

        time.sleep(60)

    def tweet_at_provider(self):
        # Check if the internet speed is less than the promised down speed
        if self.down < PROMISED_DOWN:
            # Wait for 15 seconds for the page to load
            self.driver.implicitly_wait(15)
            # Go to Twitter login page
            self.driver.get("https://twitter.com/login")
            # Find the username field and enter the email
            username = self.driver.find_element(By.CSS_SELECTOR, 'input[name="text"]')
            username.send_keys(os.getenv("email"), Keys.ENTER)
            # Wait for 10 seconds
            time.sleep(10)
            # Find the password field and enter the password
            password = self.driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')
            password.send_keys(os.getenv("password"), Keys.ENTER)
            # Wait for 10 seconds
            time.sleep(10)

            # Click the tweet button
            self.driver.find_element(By.CSS_SELECTOR, 'a[aria-label="Tweet"]').click()
            # Wait for 5 seconds
            time.sleep(5)
            # Find the write tweet field and enter the message
            write_tweet = self.driver.find_element(By.CSS_SELECTOR, 'div[data-contents="true"]')
            time.sleep(5)
            write_tweet.send_keys(
                f'Hey @SuperonlineNet, why is my internet speed {self.down}mbps when I pay for 100mbps?')
            # Wait for 5 seconds
            time.sleep(5)
            # Find the tweet button and click it
            self.driver.find_element(By.CSS_SELECTOR, 'div[data-testid="tweetButton"]').click()

        else:
            # If the internet speed is not less than the promised speed, print "Not needed"
            print("Not needed")


# Initialize the InternetSpeedTwitterBot class
bot = InternetSpeedTwitterBot()
# Get the internet speed
bot.get_internet_speed()
# Tweet at the provider
bot.tweet_at_provider()
