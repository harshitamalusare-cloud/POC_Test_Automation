import pytest
from config.credentials import TEST_USERNAME, TEST_PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.POC_page import POCPage

pytest_plugins = ["pytest_playwright"] 

@pytest.mark.parametrize("username, password", [(TEST_USERNAME, TEST_PASSWORD)])
def test_login(page, username, password):
    print("\n--- Test Started: Login ---")
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)
    poc_page = POCPage(page)

    # Step 1: Open Login Page
    login_page.open()

    # Step 2: Perform Login
    login_page.login(username, password)

    # Step 3: Wait for Dashboard
    dashboard_page.wait_for_dashboard()

    # Step 4: Verify login success
    assert dashboard_page.is_loaded(), "Dashboard not loaded properly"

    # Step 3: Navigate to POC Page
    dashboard_page.go_to_POCpage()

    # Step 4: Verify POC Page Loaded
    poc_page.wait_for_poc_page()

    # Step 5: Upload Image
    poc_page.upload_image("tests/data/POC Search.png")

    # Step 6: Keep window open to view results
    poc_page.keep_window_open()

    print("--- Test Finished Successfully ✅ ---")
