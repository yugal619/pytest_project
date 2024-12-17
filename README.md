# pytest_project
Demo on use of pytest for UI Automation using POM

🚀 Python Selenium Automation Framework (Pytest + POM Model)

Project Overview
This is a robust UI Test Automation Framework built using Python, Pytest, and Selenium. The project follows the Page Object Model (POM) design pattern to ensure code reusability, readability, and maintainability.

Test cases are automated for the sample website:
🔗 Test Pages

Key Features :
🛠️ Python + Pytest Framework: Leveraging the power of Pytest for structuring and executing test cases.

📄 Page Object Model (POM): Ensures clean and maintainable code by separating page interactions from test scripts.

🧪 Parameterized Fixtures: Used to pass test data dynamically, enabling better test coverage.

🏷️ Pytest Markers: Implemented custom markers (e.g., smoke, regression, etc.) for selective test execution.

📸 Screenshot Mechanism: Automatically captures screenshots for failed test cases for debugging purposes.

📋 Logging Mechanism: Integrated loggers to capture detailed logs of test execution.

📊 HTML Test Report: Pytest-HTML/Allure used to generate professional test execution reports.

Tech Stack
Programming Language: Python
Test Framework: Pytest
Browser Automation: Selenium
Design Pattern: Page Object Model (POM)
Reporting: Allure Reports / Pytest-HTML
Logging: Python's Logging Module

Installation and Setup
Follow these steps to set up and execute the project on your local machine:

Prerequisites
Python 3.8+
Git

1. Clone the Repository
git clone https://github.com/yugal619/pytest_project.git
cd <YOUR_PROJECT_NAME>

2. Install Dependencies
Install all required packages listed in requirements.txt:

pip install -r requirements.txt

3. Run Test Cases
Execute test cases using Pytest:

pytest tests/ --html=reports/report.html --self-contained-html

Run Specific Tests:
pytest -m "smoke"          # Run tests marked as smoke
pytest -k "home_page"      # Run tests containing 'home_page' in name

Features in Detail
1. Page Object Model (POM)
Each web page is represented as a class under the pages/ directory. This ensures reusability of page-specific methods.


Contributing
Contributions are welcome! If you have suggestions or ideas to enhance the framework, feel free to create a Pull Request.

Contact
📧 Email: yugal.sinha619@gmail.com
🔗 LinkedIn: https://www.linkedin.com/in/yugal-sinha-629941124/

SEO Optimized Keywords
To ensure visibility on search engines like Google:

Python Selenium Automation Framework
Pytest Framework with POM
Selenium Test Automation
Screenshot Mechanism in Pytest
Test Reporting with Pytest-HTML and Allure
Automated UI Testing using Python
