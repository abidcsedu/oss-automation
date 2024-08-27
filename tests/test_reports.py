import os
import dotenv
import pytest
from playwright.sync_api import Playwright, sync_playwright, expect

@pytest.fixture(scope="module")
def test_report_clicks(env, playwright: Playwright):

    dotenv.load_dotenv()
    login_page = os.getenv('FRONTEND_LOGIN')
    admin = os.getenv('ADMIN')
    passwd = os.getenv('ADMIN_PASSWORD')

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(login_page)
    page.get_by_placeholder("Email").click()
    page.get_by_placeholder("Email").fill(admin)
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill(passwd)
    page.get_by_role("button", name="Log In").click()
    page.get_by_role("button", name="Reports").click()

    page.locator("//span[@class='pro-item-content' and text()='Application Summary']").click()
    expect(page.locator("//div[@id='table-container']//tbody")).to_be_visible()

    page.locator("//span[@class='pro-item-content' and text()='Work Permit Summary']").click()
    expect(page.locator("//div[@id='table-container']//tbody")).to_be_visible()

    page.locator("//span[@class='pro-item-content' and text()='Visa Recommendation Summary']").click()
    expect(page.locator("//div[@id='table-container']//tbody")).to_be_visible()

    page.locator("//span[@class='pro-item-content' and text()='Users Summary']").click()
    expect(page.locator("//div[@id='table-container']//tbody")).to_be_visible()

    page.locator("//span[@class='pro-item-content' and text()='Import Permit Summary']").click()
    expect(page.locator("//div[@id='table-container']//tbody")).to_be_visible()

    page.locator("//span[@class='pro-item-content' and text()='Export Permit Summary']").click()
    expect(page.locator("//div[@id='table-container']//tbody")).to_be_visible()

    page.locator(f"//span[@class='pro-item-content' and text()=\"Investor's Info Summary\"]").click()
    expect(page.locator("//div[@class='apa-report-table']//tbody")).to_be_visible()

    page.locator("//span[@class='pro-item-content' and text()='Investment Clearance Summary']").click()
    expect(page.locator("//div[@id='table-container']//tbody")).to_be_visible()

    page.locator("li").filter(has_text="SUPER").locator("#header-icon-container").click()
    page.locator("div").filter(has_text=re.compile(r"^Logout$")).nth(1).click()

    # ---------------------
    context.close()
    browser.close()
