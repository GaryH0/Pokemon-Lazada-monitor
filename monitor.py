import urllib.request
import re
import json

URL = (
    "https://www.lazada.sg/products/"
    "pokemon-trading-card-game-mega-evolution-ascended-heroes-"
    "booster-bundle-limit-1-per-person-i13696744288-s124594658123.html"
)

headers = {
    "User-Agent": (
        "Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) "
        "AppleWebKit/605.1.15 Version/18.0 Mobile/15E148 Safari/604.1"
    ),
    "Accept-Language": "en-SG,en;q=0.9",
}

request = urllib.request.Request(URL, headers=headers)

with urllib.request.urlopen(request, timeout=20) as response:
    page = response.read().decode("utf-8", errors="ignore")
    print("HTTP status:", response.status)
    print("Response URL:", response.geturl())

print("Page size:", len(page))
print("Ascended Heroes:", bool(re.search(r"Ascended Heroes", page, re.I)))

checks = {
    "Buy Now": r"Buy Now",
    "Add to Cart": r"Add to Cart",
    "Out of Stock": r"Out of Stock",
    "Sold Out": r"Sold Out",
    "stock": r"stock",
    "quantity": r"quantity",
    "availability": r"availability",
    "inventory": r"inventory",
    "skuId": r"skuId",
    "itemId": r"itemId",
}

for name, pattern in checks.items():
    matches = list(re.finditer(pattern, page, re.I))
    print(f"{name}: {len(matches)}")

print("\n=== JSON-LIKE STOCK FRAGMENTS ===")

patterns = [
    r'.{0,120}"stock".{0,250}',
    r'.{0,120}"quantity".{0,250}',
    r'.{0,120}"availability".{0,250}',
    r'.{0,120}"inventory".{0,250}',
    r'.{0,120}"skuId".{0,250}',
    r'.{0,120}"itemId".{0,250}',
]

for pattern in patterns:
    matches = re.findall(pattern, page, re.I | re.S)
    for m in matches[:5]:
        print(m.replace("\n", " ")[:500])
        print("---")
