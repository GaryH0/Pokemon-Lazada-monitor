import urllib.request
import re

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

print("Page size:", len(page))

terms = [
    "sellable",
    "stockMap",
    "stockStatus",
    "stockStatusV2",
    "availableStock",
    "sellableStock",
    "bizData",
    "skuInfos",
    "skuCore",
    "disabled",
    "disable",
    "purchaseQuantity",
    "124594658123",
]

for term in terms:
    print(f"\n=== {term} ===")
    matches = list(re.finditer(term, page, re.I))
    print("matches:", len(matches))

    for match in matches[:8]:
        start = max(0, match.start() - 400)
        end = min(len(page), match.end() + 700)
        snippet = page[start:end].replace("\n", " ")
        print(snippet[:1200])
        print("---")
