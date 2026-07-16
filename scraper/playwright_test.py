from playwright.sync_api import sync_playwright

URL = "https://www.athletic.net/CrossCountry/meet/256297/results/1018811"

with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=False,
        channel="chrome"
    )

    page = browser.new_page()

    page.on(
        "response",
        lambda response: print(response.status, response.url)
    )

    print("Opening page...")

    page.goto(URL)

    input("Press Enter to close...")

    browser.close()