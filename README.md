# 🚀 Selenium + Behave Automation Framework

## 📌 Project Overview

This project is a **Selenium + Behave automation framework** for UI testing.
It follows **Behavior-Driven Development (BDD)** using **Gherkin syntax** and generates reports using **Allure**.

---

## ⚙️ Features

✅ **BDD with Behave & Gherkin** – Easily write human-readable test cases
✅ **Selenium WebDriver** – Automate browser interactions
✅ **Page Object Model (POM)** – Maintain clean and reusable code
✅ **Allure Reporting** – Generate detailed test reports
✅ **Headless Mode Support** – Run tests faster without a UI

---

## 🔧 Setup

1️⃣ **Create and activate a virtual environment**

```sh

python -m venv .venv
source .venv/bin/activate  # macOS/Linux
.\.venv\Scriptsctivate   # Windows
2️⃣ Install dependencies 
pip install -r requirements.txt

list of requirements 
selenium
behave #→ for BDD
webdriver-manager #→ for diff browser
allure-behave #→ for reports
# for test_evidence
opencv-python #→ Used for saving video recordings (cv2.VideoWriter).
pyautogui #→ Captures screen frames (pyautogui.screenshot()).
numpy #→ Converts screenshots into OpenCV-compatible format (np.array())
```

---

## 🚀 Running Tests

**behave**
``python -m behave``
**Run tests with Allure reporting:**
``allure generate reports/allure-results/ --clean -o reports/allure-report``
**Generate the Allure report:**
``allure serve reports/allure-results or allure open reports/allure-report``

---

## 📊 Test Reports

Allure Reports – reports/allure-results and reports/allure-report
HTML Reports – reports/results.html
CSV Reports – reports/results.csv

---

## 👨‍💻 Author

📌 Mike EJ Redondo
📧 your.email@example.com
🔗 LinkedIn/GitHub (if applicable)
