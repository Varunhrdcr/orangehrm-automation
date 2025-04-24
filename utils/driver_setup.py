from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def get_driver():
    # Set up Chrome options
    options = webdriver.ChromeOptions()
    options.headless = False  # Run in non-headless mode so you can see the browser

    # Set up the Chrome driver with the correct version using ChromeDriverManager
    service = Service(ChromeDriverManager().install())

    # Initialize the WebDriver
    driver = webdriver.Chrome(service=service, options=options)

    # Maximize window (optional)
    driver.maximize_window()

    # Return the driver object
    return driver
