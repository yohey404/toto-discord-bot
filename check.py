import re
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
browser = p.chromium.launch(headless=True)
page = browser.new_page()

```
page.goto(
    "https://toto.rakuten.co.jp/big/carryover/",
    wait_until="networkidle"
)

text = page.locator("body").inner_text()
browser.close()
```

nums = re.findall(r'([\d,]+)円', text)

carry = []
for n in nums:
value = int(n.replace(",", ""))
if value > 100000000:
carry.append(value)

print("BIG:", carry[0])
print("MEGA BIG:", carry[1])
print("100円BIG:", carry[2])
