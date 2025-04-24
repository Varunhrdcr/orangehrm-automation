from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.pim_tab = (By.XPATH, "//span[text()='PIM']")
        self.profile_icon = (By.XPATH, "//span[@class='oxd-userdropdown-tab']")
        self.logout_button = (By.XPATH, "//a[text()='Logout']")
    
    def go_to_pim(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            pim_element = wait.until(EC.element_to_be_clickable(self.pim_tab))
            pim_element.click()
            print("PIM tab clicked successfully")
        except Exception as e:
            print("Failed to click PIM tab:", e)
    
    def logout(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.element_to_be_clickable(self.profile_icon)).click()
            wait.until(EC.element_to_be_clickable(self.logout_button)).click()
            print("Logged out successfully")
        except Exception as e:
            print("Failed to logout:", e)
