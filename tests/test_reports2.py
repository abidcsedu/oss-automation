import os
import re
import dotenv
import pytest
from playwright.sync_api import Playwright, expect
from locators import Locators

@pytest.mark.parametrize("nohead", [False])
def test_report_clicks(playwright: Playwright, nohead: bool):
    dotenv.load_dotenv()
    login_page = os.getenv('FRONTEND_LOGIN')
    admin = os.getenv('ADMIN')
    passwd = os.getenv('ADMIN_PASSWORD')
    browser = playwright.chromium.launch(headless=nohead)
    context = browser.new_context()

    page = context.new_page()
    page.goto(login_page)
    page.get_by_placeholder("Email").click()
    page.get_by_placeholder("Email").fill(admin)
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill(passwd)

    page.get_by_role("button", name="Log In").click()

    print("Navigating to Reports...")
    page.get_by_role("button", name="Reports").click()

    for report in Locators.REPORTS:
        print(f"Clicking on report: {report}")
        page.locator(report).click()
        expect(page.locator(Locators.TABLE_CONTAINER)).to_be_visible()
        print(f"Report {report} is visible.")

    print(f"Clicking on report: {Locators.APA_REPORT}")
    page.locator(Locators.APA_REPORT).click()
    expect(page.locator(Locators.APA_CONTAINER)).to_be_visible()
    print(f"Report {Locators.APA_REPORT} is visible.")

    print(f"Clicking on report: {Locators.IC_REPORT}")
    page.locator(Locators.IC_REPORT).click()
    expect(page.locator(Locators.TABLE_CONTAINER)).to_be_visible()
    print(f"Report {Locators.IC_REPORT} is visible.")

    print("Logging out...")
    page.locator("li").filter(has_text="Admin").locator("#header-icon-container").click()
    page.locator("div").filter(has_text=re.compile(r"^Logout$")).nth(1).click()

    context.close()
    browser.close()
