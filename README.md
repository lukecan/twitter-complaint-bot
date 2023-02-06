# Internet Speed Twitter Bot

A python script that uses selenium webdriver to check the internet speed and tweet at the service provider if the speed is below the promised speed.

## Requirements

- Python 3.x
- selenium
- dotenv
- ChromeDriver
- Usage

Clone the repository
Create a `.env` file in the same directory as the script and add the following environment variables:
- `path`: Path to the ChromeDriver binary
- `email`: Twitter email to use for logging in
- `password`: Twitter password to use for logging in
- Install the required packages with `pip install -r requirements.txt`
Run the script with python `main.py`

## Constants

The promised download and upload speeds are set as constants:

- `PROMISED_DOWN` = 50
- `PROMISED_UP` = 10

## Code Walkthrough

- The script loads environment variables from the `.env` file using `load_dotenv` from the dotenv library.
- The ChromeDriver is initialized with the path from the environment variables.
- The `get_internet_speed` method navigates to speedtest.net, clicks the "Go" button, waits for the speed test to complete and retrieves the download and upload speeds.
- The `tweet_at_provider method checks if the download speed is less than the promised speed, logs into Twitter, and tweets at the service provider if the speed is below the promised speed.