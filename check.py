import re
import requests
import os
from playwright.sync_api import sync_playwright

WEBHOOK = os.environ["https://discord.com/api/webhooks/1513748913020993657/O3nPQ8_lhLJ-WdnMLflpY8JFl2GzwGTOV_VGogW_wzIeVotZNXLvIke2JzaHsVznZ5tg"]

with sync_playwright() as p:
browser = p.chromium.launch(headless=True)
page = browser.new_page()

page.goto(
    "https://toto.rakuten.co.jp/big/carryover/",
    wait_until="networkidle"
)

text = page.locator("body").inner_text()

browser.close()

nums = re.findall(r'([\d,]+)円', text)

carry = []

for n in nums:
value = int(n.replace(",", ""))
if value > 100000000:
carry.append(value)

print(carry)

big = carry[0]
mega = carry[1]
big100 = carry[2]

msg = []

if mega >= 10000000000:
msg.append(f"🎉 MEGA BIG 100億円到達\n{mega:,}円")

if big >= 5000000000:
msg.append(f"🎉 BIG 50億円到達\n{big:,}円")

if big100 >= 500000000:
msg.append(f"🎉 100円BIG 5億円到達\n{big100:,}円")

if msg:
requests.post(
WEBHOOK,
json={"content": "\n\n".join(msg)},
timeout=30
)
