from playwright.sync_api import sync_playwright

URL = "https://www.athletic.net/CrossCountry/meet/256297/results/1018811"

with sync_playwright() as p:

    context = p.chromium.launch_persistent_context(
        user_data_dir="playwright_profile",
        headless=False,
        channel="chrome",
    )

    page = context.new_page()

    print("Opening page...")
    page.goto(URL)

    print(page.title())

    input("Press Enter to close...")

    context.close()