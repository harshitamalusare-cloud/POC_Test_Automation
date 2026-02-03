from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_input = page.locator("#email")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("button:has-text('Login')")

    def open(self):
        print("[ACTION] Opening login page...")
        self.page.goto("https://agent.goloti.com/login")
        self.page.wait_for_load_state("domcontentloaded")
        print("[PASS] Login page loaded successfully.")

    def login(self, username: str, password: str):
        print(f"[ACTION] Filling in email: {username}")
        self.email_input.fill(username)

        print("[ACTION] Filling in password...")
        self.password_input.fill(password)

        print("[ACTION] Clicking on Login button...")
        self.login_button.click()
        self.page.wait_for_load_state("networkidle")
        print("[PASS] Login form submitted successfully.")
