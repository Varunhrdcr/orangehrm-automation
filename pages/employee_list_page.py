from selenium.webdriver.common.by import By

class EmployeeListPage:
    def __init__(self, driver):
        self.driver = driver

    def verify_employee(self, name):
        rows = self.driver.find_elements(By.XPATH, "//div[@role='row']")
        for row in rows:
            if name.lower() in row.text.lower():
                print(f"{name} Verified ✅")
                return True
        print(f"{name} Not Found ❌")
        return False
