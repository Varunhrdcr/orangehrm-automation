from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import traceback
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.pim_page import PIMPage

print("Test started")

# Set up Chrome driver
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.headless = False 
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()

try:
    print("Opening the OrangeHRM login page...")
    driver.get("https://opensource-demo.orangehrmlive.com/")
    
    login = LoginPage(driver)
    login.login("Admin", "admin123")
    print("Login successful")

    dashboard = DashboardPage(driver)
    print("Navigating to PIM module...")
    dashboard.go_to_pim()

    pim = PIMPage(driver)

    employees = [("Zzeeshan", "Doe"), ("Zyaeem", "Smith"), ("Zxyan", "Brown")]
    full_names = [f"{first} {last}" for first, last in employees]
    print(f"Adding employees: {', '.join(full_names)}")
    
    for first, last in employees:
        pim.add_employee(first, last)

    print("Verifying employees in the list...")
    for full_name in full_names:
        if pim.verify_employee_in_list(full_name):
            print(f"Employee verification successful: {full_name}")
        else:
            print(f"Employee verification failed: {full_name}")

    print("Logging out...")
    dashboard.logout()
    print("Test finished successfully")

except Exception as e:
    print("Test failed:", str(e))
    traceback.print_exc()

finally:
    driver.quit()
