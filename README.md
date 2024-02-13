# Python Automation Framework

This is a Python-based TDD automation framework that includes methods for handling APIs, database interactions, UI testing using Selenium, and additional utility modules for working with Parquet files, Databricks, and cluster connectivity. This framework is designed to facilitate test automation for web applications and data processing by combining different testing aspects and utility functions into a cohesive and easy-to-use structure.

## Table of Contents

1. [Project Structure](#project-structure)
2. [Prerequisites](#prerequisites)
3. [Getting Started](#getting-started)
4. [Additional Utility Modules](#additional-utility-modules)
5. [Test Execution](#test-execution)
6. [Reporting](#reporting)
7. [Contributing](#contributing)
8. [License](#license)

## Project Structure
1. UDP_Automation_Project/
   1. reports/
      1. report.html
   2. resources/
      1. driver/
      2. testdata/
         1. parquet_files/
         2. schemas/
      3. config.py
   3. test/
      1. locators/
         1. login_locators.py
         2. homepage_locators.py
      2. pages/
         1. base_page.py
         2. login_page.py
         3. home_page.py 
      3. tests/
         1. test_main.py
      4. utils/
         1. parquet_utils.py
         2. databricks_utils.py
         3. cluster_utils.py
         4. compare_utils.py
   4. conftest.py
   5. execute_tests.py
   6. pytest.ini
   7. README.md
   8. requirements.txt

- `reports/`: Store generated test reports.
- `resources`: Stored all the required drivers, testdata and config files.
- `testdata/Schemas`: This directory houses all the schemas required for parquet file creation
- `testdata/parquet_files`: This directory stores all the parquet files generated for further usage. 
- `config/`: Store configuration files.
- `test/locators/`: This directory houses files that define locators for UI elements. These locators are used in your UI Selenium tests to identify and interact with specific elements on web pages.
- `test/pages/`: This directory contains modules that represent individual web pages or sections of a web application. These modules encapsulate the functionality and interactions associated with specific pages, making your UI tests more organized and maintainable.
- `test/tests/`: This directory is where you place your actual test cases. These test cases use the locators, utilities, and page objects defined in the other directories to perform specific test scenarios, helping ensure the functionality and reliability of your application.
- `test/utils/`: Within this directory, you can find utility modules that contain functions and helper methods used across different testing modules. These utilities help streamline common operations and maintain clean and reusable code.
- `parquet_utils.py`: Provides methods for working with Parquet files.
- `databricks_utils.py`: Offers Databricks connectivity methods.
- `cluster_utils.py`: Includes functions for creating and managing cluster connectivity.
- `compare_utils.py`: Includes all the methods required for data comparison.
- `conftest.py`: Handles driver setup and database initiation.
- `execute_tests.py`: Includes argument parser declarations for test execution.
- `pytest.ini`: Includes all the pytest markers.
- `README.md`: Documentation for the automation framework.
- `requirements.txt`: Lists project dependencies.

## Prerequisites

Before using this automation framework, ensure you have the following prerequisites installed:

- Python 3.x
- Pip (Python package manager)
- Required Python packages (install using `pip install -r requirements.txt`)
- Web browsers (for UI Selenium testing)
- API endpoints and authentication details
- Database connection details
- Configuration for Parquet files
- Databricks authentication and cluster details

## Getting Started

1. Clone this repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Configure API and database connection details in the `config.py` file under resources folder.
4. Set up the UI testing environment by configuring browser drivers.
5. Ensure that Parquet, Databricks, and cluster connectivity configurations are correctly set in the respective utility modules.
6. Utilize `conftest.py` for driver setup and database initiation.

## Additional Utility Modules
1. `parquet_utils.py`: Includes methods for creating and interacting with Parquet files.
2. `databricks_utils.py`: Provides connectivity to Databricks using the Simba Spark driver.
3. `cluster_utils.py`: Includes functions for creating and managing cluster connectivity.
4. `conftest.py`: Handles driver setup and database initiation.

## Test Execution
Use `execute_tests.py` to configure and execute tests. It provides argument parser declarations to facilitate test execution and customization.

## Reporting
Test reports and logs will be generated in the reports folder for better tracking and debugging.

## Contributing
We welcome contributions to this automation framework. If you have improvements, bug fixes, or new features to add, please create a pull request.

## License
This automation framework is open-source. Download it and feel free to use, modify, and distribute it as needed.

With this update, your README now includes information about the `conftest.py` and `execute_tests.py` files, which are essential for the setup and execution of tests within your automation framework.
