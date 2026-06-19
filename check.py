from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto(
        "https://toto.rakuten.co.jp/big/carryover/",
        wait_until="networkidle"
    )

    text = page.locator("body").inner_text()

    print(text[:5000])

    browser.close()
