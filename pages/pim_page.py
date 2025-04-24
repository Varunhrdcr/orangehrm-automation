from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class PIMPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_button = (By.XPATH, "//button[normalize-space()='Add']")
        self.first_name_input = (By.NAME, "firstName")
        self.last_name_input = (By.NAME, "lastName")
        self.save_button = (By.XPATH, "//button[@type='submit']")
        self.employee_name_field = (By.XPATH, "//input[@placeholder='Type for hints...']")
        self.search_button = (By.XPATH, "//button[@type='submit']")
        self.results = (By.XPATH, "//div[@role='rowgroup']//div[@role='row']")

    def add_employee(self, first_name, last_name):
        wait = WebDriverWait(self.driver, 20)

        # Navigate to PIM employee list
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")
        wait.until(EC.presence_of_element_located((By.XPATH, "//h6[text()='PIM']")))

        # Click Add
        wait.until(EC.element_to_be_clickable(self.add_button)).click()

        # Enter details
        wait.until(EC.visibility_of_element_located(self.first_name_input)).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)

        # Click Save
        self.driver.find_element(*self.save_button).click()

        # Wait until redirected back to PIM page
        wait.until(EC.presence_of_element_located((By.XPATH, "//h6[text()='PIM']")))
        time.sleep(1)

    def verify_employee_in_list(self, full_name):
        wait = WebDriverWait(self.driver, 15)
        try:
            self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")

            search_input = wait.until(EC.visibility_of_element_located(self.employee_name_field))
            search_input.clear()
            search_input.send_keys(full_name)

            self.driver.find_element(*self.search_button).click()
            wait.until(EC.presence_of_element_located(self.results))

            results = self.driver.find_elements(*self.results)
            first_last = full_name.lower().split()

            for result in results:
                row_text = result.text.lower()
                if all(name in row_text for name in first_last):
                    return True

            return False
        except Exception:
            return False
