class Locators:
    TABLE_CONTAINER = "//div[@id='table-container']//tbody"
    REPORTS = [
        "//span[@class='pro-item-content' and text()='Application Summary']",
        "//span[@class='pro-item-content' and text()='Work Permit Summary']",
        "//span[@class='pro-item-content' and text()='Visa Recommendation Summary']",
        "//span[@class='pro-item-content' and text()='Users Summary']",
        "//span[@class='pro-item-content' and text()='Import Permit Summary']",
        "//span[@class='pro-item-content' and text()='Export Permit Summary']",
    ]
    APA_CONTAINER = "//div[@class='apa-report-table']//tbody"
    APA_REPORT="//span[@class='pro-item-content' and text()=\"Investor's Info Summary\"]"
    IC_REPORT="//span[@class='pro-item-content' and text()='Investment Clearance Summary']"
