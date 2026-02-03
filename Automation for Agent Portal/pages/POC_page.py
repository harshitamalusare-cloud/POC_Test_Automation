from playwright.sync_api import Page, expect

class POCPage:
    def __init__(self, page: Page):
        self.page = page

        # Expected URL
        self.expected_poc_url = "https://agent.goloti.com/poc"

        # ✅ Upload Image XPath (example)
        self.upload_input = page.locator("//input[@type='file']")

        # Optional: Upload button if needed
        self.upload_button = page.locator("//button[contains(text(),'Upload')]")

        # Start Search button
        self.start_search_button = page.locator("//button[text()='Start Search']")

    def wait_for_poc_page(self):
        print("[ACTION] Waiting for POC page...")
        expect(self.page).to_have_url(self.expected_poc_url, timeout=15000)
        print("[PASS] POC Page loaded successfully ✅")

    def upload_image(self, file_path: str):
        print("[ACTION] Uploading image...")

        # Upload file directly
        self.upload_input.set_input_files(file_path)

        print("[PASS] Image selected successfully ✅")

        # Click Start Search button
        self.start_search_button.click()
        print("[PASS] Start Search button clicked ✅")

    def keep_window_open(self):
        """Keep the window open indefinitely until user closes it manually"""
        print("[ACTION] Keeping window open indefinitely...")
        print("[INFO] Window will stay open. Close the browser manually when done.")
        self.page.wait_for_load_state("networkidle")
        # Keep the browser context alive indefinitely
        while True:
            self.page.wait_for_timeout(1000)
