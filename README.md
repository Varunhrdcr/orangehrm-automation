# 🧪 OrangeHRM Automation with Selenium

Automated testing script for **OrangeHRM** using **Python** and **Selenium WebDriver**. This project performs end-to-end automation of login, employee addition, and verification functionalities on the [OrangeHRM Demo site](https://opensource-demo.orangehrmlive.com/).

## 🚀 Features

- ✅ Automates login using valid credentials
- 👥 Adds multiple employees dynamically
- 🔍 Verifies employee existence in the list
- 📄 Structured using Page Object Model (POM)
- 🧼 Clean console output for better debugging

## 🧰 Tech Stack

- **Python 3.x**
- **Selenium WebDriver**
- **ChromeDriver** (via `webdriver-manager`)
- **Page Object Model (POM)** design pattern

## 📁 Folder Structure

```
orangehrm-automation/
│
├── pages/
│   ├── login_page.py        # Login page actions
│   ├── dashboard_page.py    # Navigation actions
│   └── pim_page.py          # Add & verify employee
│
├── test_orangehrm.py        # Main test script
├── requirements.txt         # Dependencies
└── README.md                # You're here!
```

## 🛠️ Setup Instructions

1. **Clone this repository**
   ```bash
   git clone https://github.com/Varunhrdcr/orangehrm-automation.git
   cd orangehrm-automation
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the test**
   ```bash
   python test_orangehrm.py
   ```

> 💡 Make sure Google Chrome is installed. `webdriver-manager` will handle the driver.

## 🧪 Sample Output

```
Test started
Opening the OrangeHRM login page...
Login successful
Navigating to PIM module...
Adding employees: John Doe, Jane Smith, Michael Brown
Verifying employees in the list...
Employee verification successful: John Doe
Employee verification successful: Jane Smith
Employee verification successful: Michael Brown
Logging out...
Test finished successfully
```

## 👤 Author

- **Varun Sharma**  
  💼 B.Tech CSE | 🔍 Aspiring QA Engineer & Data Analyst  
  📍 Bangalore, India  
  📧 varunsharmapn2003@gmail.com  
  🔗 [LinkedIn](https://linkedin.com/in/varunsharmapn2003)

---

Feel free to ⭐ the repo if you found it useful!
