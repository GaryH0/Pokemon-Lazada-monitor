import urllib.request
import re
import html as html_lib

URL = "https://s.lazada.sg/s.Tfr9A?c=w"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) "
        "AppleWebKit/605.1.15 Version/18.0 Mobile/15E148 Safari/604.1"
    )
}

request = urllib.request.Request(URL, headers=headers)

with urllib.request.urlopen(request, timeout=20) as response:
    page = response.read().decode("utf-8", errors="ignore")
    print("HTTP status:", response.status)
    print("Response URL:", response.geturl())

print("Page size:", len(page))
print("Ascended Heroes:", "Ascended Heroes" in page)

print("\n=== POSSIBLE PRODUCT URLS ===")

urls = re.findall(r'https?://[^"\'<>\\ ]+', page)

seen = set()

for raw_url in urls:
    clean_url = html_lib.unescape(raw_url)

    if (
        "lazada.sg/products/" in clean_url.lower()
        or "lazada.sg/-i" in clean_url.lower()
        or "lazada.sg/products" in clean_url.lower()
    ):
        if clean_url not in seen:
            seen.add(clean_url)
            print(clean_url[:1000])

print("\n=== PRODUCT / SKU IDENTIFIERS ===")

patterns = [
    r'"itemId"\s*:\s*"?([0-9]+)"?',
    r'"item_id"\s*:\s*"?([0-9]+)"?',
    r'"productId"\s*:\s*"?([0-9]+)"?',
    r'"product_id"\s*:\s*"?([0-9]+)"?',
    r'"skuId"\s*:\s*"?([0-9]+)"?',
    r'"sku_id"\s*:\s*"?([0-9]+)"?',
    r'"sellerId"\s*:\s*"?([0-9]+)"?',
]

for pattern in patterns:
    matches = re.findall(pattern, page, re.I)

    if matches:
        print(pattern, "=>", list(dict.fromkeys(matches))[:10])

print("\n=== LINKS AROUND ASCENDED HEROES ===")

for match in re.finditer("Ascended Heroes", page, re.I):
    start = max(0, match.start() - 500)
    end = min(len(page), match.end() + 1000)

    snippet = page[start:end]
    snippet = html_lib.unescape(snippet)
    snippet = snippet.replace("\n", " ")

    print(snippet[:1600])
    print("---")
