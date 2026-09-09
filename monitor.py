import urllib.request
import re

URL = "https://s.lazada.sg/s.Tfr9A?c=w"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) "
        "AppleWebKit/605.1.15 Version/18.0 Mobile/15E148 Safari/604.1"
    )
}

request = urllib.request.Request(URL, headers=headers)

with urllib.request.urlopen(request, timeout=20) as response:
    html = response.read().decode("utf-8", errors="ignore")

print("Page size:", len(html))
print("Ascended Heroes:", bool(re.search(r"Ascended Heroes", html, re.I)))

keywords = [
    "stock",
    "quantity",
    "available",
    "availability",
    "soldout",
    "sold out",
    "out of stock",
    "inventory",
    "buy now",
    "add to cart",
]

for keyword in keywords:
    print(f"\n=== {keyword.upper()} ===")
    matches = list(re.finditer(keyword, html, re.I))
    print("matches:", len(matches))

    for match in matches[:5]:
        start = max(0, match.start() - 150)
        end = min(len(html), match.end() + 250)
        snippet = html[start:end].replace("\n", " ")
        print(snippet)
