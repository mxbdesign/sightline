from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    for version in ["v1", "v2", "v3"]:
        page = browser.new_page()
        page.goto(f"http://localhost:8000/{version}.html")
        page.wait_for_timeout(2000)
        page.screenshot(path=f"/home/jules/verification/{version}_texture_fixed.png")
        print(f"Captured {version}_texture_fixed.png")
    browser.close()
