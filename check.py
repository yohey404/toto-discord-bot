import requests
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    page.goto(
        "https://toto.rakuten.co.jp/big/carryover/",
        wait_until="networkidle"
    )

    print(page.title())

    browser.close()
