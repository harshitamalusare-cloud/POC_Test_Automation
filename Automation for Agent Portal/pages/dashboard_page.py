from playwright.sync_api import Page, expect

class DashboardPage:
    def __init__(self, page: Page):
        self.page = page
        self.expected_dashboard_url = "https://agent.goloti.com/dashboard/overview"
        self.dashboard_menu = page.locator("a[href='/artists']")  # or any element visible on dashboard

    def is_loaded(self) -> bool:
        """Checks if dashboard URL and elements are visible."""
        try:
            # Verify the URL
            current_url = self.page.url
            if self.expected_dashboard_url not in current_url:
                return False

            # Verify a visible element on dashboard
            return self.dashboard_menu.is_visible()
        except:
            return False

    def wait_for_dashboard(self):
        """Waits for the dashboard URL to load successfully after login."""
        print("[ACTION] Waiting for dashboard URL to load...")
        expect(self.page).to_have_url(self.expected_dashboard_url, timeout=15000)
        self.page.wait_for_load_state("networkidle")
        print("[PASS] Login successful and dashboard loaded ✅")

    def go_to_artists(self):
        self.page.click("a[href='/artists']")

    def go_to_prospects(self):
        self.page.click("a[href='/prospects']")
    
    def go_to_POCpage(self):
        self.page.click("a[href='/poc']")
    
    def upload_image(self, file_path: str):
        print("[ACTION] Uploading image...")

