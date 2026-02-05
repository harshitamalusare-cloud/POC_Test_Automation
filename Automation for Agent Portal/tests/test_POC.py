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
        """Wait for POC results to load and verify success or failure"""
        print("[ACTION] Waiting for POC search results...")
        
        try:
            # Define result container locator
            result_container = self.page.locator("//*[@class='flex flex-col gap-4 w-full']")
            
            # Wait for result container to be visible
            print("[ACTION] Waiting for results container to appear...")
            result_container.wait_for(state="visible", timeout=60000)
            print("[INFO] Results container loaded")
            
            # Wait for page to stabilize
            self.page.wait_for_load_state("networkidle", timeout=30000)
            
            # Check if results are visible
            if result_container.is_visible():
                print("[PASS] POC search results displayed successfully ✅")
                return True
            else:
                print("[FAIL] Results not displayed ❌")
                return False
                
        except Exception as e:
            print(f"[FAIL] {str(e)} ❌")
            return False
