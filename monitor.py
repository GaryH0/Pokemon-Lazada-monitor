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

try:
    with urllib.request.urlopen(request, timeout=20) as response:
        html = response.read().decode("utf-8", errors="ignore")
        final_url = response.geturl()

    print("HTTP request successful")
    print("Final URL:", final_url)
    print("Page size:", len(html))
    print("Contains 'Ascended Heroes':",
          bool(re.search(r"Ascended Heroes", html, re.I)))
    print("Contains 'Buy Now':",
          bool(re.search(r"Buy Now", html, re.I)))
    print("Contains 'out of stock':",
          bool(re.search(r"out of stock", html, re.I)))

except Exception as e:
    print("REQUEST FAILED")
    print(type(e).__name__, str(e))
    raise
