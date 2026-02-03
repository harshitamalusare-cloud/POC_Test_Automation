import pytest
from playwright.sync_api import sync_playwright
from config.credentials import TEST_USERNAME, TEST_PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
# Added # type: ignore to bypass potential module resolution errors in the editor,
# while the package is still installed and used by Pytest at runtime.

# -----------------------------------------------------------------------------
# conftest.py
# Purpose: Defines Pytest fixtures (setup/teardown) for Playwright context.
# -----------------------------------------------------------------------------

@pytest.fixture(scope="session")
def playwright_instance():
    """Initializes and tears down the Playwright engine."""
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(playwright_instance):
    """Launches and closes the Chromium browser instance."""
    # Setting headless=False allows you to visually watch the test execution
    browser = playwright_instance.chromium.launch(headless=False)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def page(browser):
    """Creates a new browser context and page for each test function."""
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page", None)
        if page:
            screenshot_path = f"screenshots/{item.name}.png"
            print(f"[HOOK] Capturing screenshot on failure: {screenshot_path}")
            page.screenshot(path=screenshot_path)

@pytest.fixture(scope="session")
def logged_in_page(browser):
    """
    Fixture to return a logged-in page object for all tests.
    """
    page = browser.new_page()
    
    # Initialize page objects
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)

    # Perform login
    login_page.open()
    login_page.login(TEST_USERNAME, TEST_PASSWORD)
    dashboard_page.wait_for_dashboard()
    
    yield page  # This page is now logged in and ready for all tests

    page.close()
