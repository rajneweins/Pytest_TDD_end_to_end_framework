import argparse
import pytest


def main(args):
    # Set the required configurations for the driver
    browser = args.browser
    headless_mode = args.headless

    # Set the test file or directory to run
    # test_file_or_directory = args.test
    test_file_or_directory = "test/tests/test_main.py"
    # Set the HTML report path
    report_path = args.html  # Changed from args.report

    # Pass the configurations as command-line arguments to pytest
    pytest_args = [
        "--browser=" + browser,
        "--html=" + report_path
    ]
    if headless_mode:
        pytest_args.append("--headless")

    # Add markers here
    if args.markers:
        pytest_args.extend(["-m", args.markers])

    pytest_args.append(test_file_or_directory)

    # Run the tests and generate the HTML report
    pytest.main(pytest_args)


if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Test Execution')
    parser.add_argument('--browser', type=str, default='chrome',
                        help='Type of browser (chrome/firefox)')
    parser.add_argument('--headless', action='store_true',
                        help='Enable headless mode')
    parser.add_argument('--html', type=str,
                        default='reports/report.html', help='HTML report path')
    parser.add_argument('--markers', type=str, default='test_marker',
                        help='Run tests with specific markers')
    main(args=parser.parse_args())

    # pytest.main(["-v", "--html=reports/report.html"])
    # pytest.main(["--browser", "chrome", "--headless", "False",
    #              # "--report", "reports/report.html",
    #              "-markers", 'smoke'])
