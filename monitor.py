from playwright.sync_api import sync_playwright

URL = (
    "https://www.lazada.sg/products/"
    "pokemon-trading-card-game-mega-evolution-ascended-heroes-"
    "booster-bundle-limit-1-per-person-i13696744288-s124594658123.html"
)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    page = browser.new_page(
        locale="en-SG",
        viewport={"width": 390, "height": 844},
    )

    page.goto(URL, wait_until="domcontentloaded", timeout=60000)
    page.wait_for_timeout(8000)

    text = page.locator("body").inner_text()

    print("Final URL:", page.url)
    print("Page title:", page.title())
    print("Body length:", len(text))

    phrases = [
        "Item chosen is out of stock",
        "Out of stock",
        "Add to Cart",
        "Buy Now",
        "Find similar products",
        "Cancel Reminder",
        "Ascended Heroes",
    ]

    for phrase in phrases:
        print(f"{phrase}: {phrase.lower() in text.lower()}")

    print("\n=== RELEVANT TEXT ===")

    for line in text.splitlines():
        lower = line.lower()

        if any(
            keyword in lower
            for keyword in [
                "stock",
                "cart",
                "buy now",
                "reminder",
                "similar product",
                "ascended heroes",
            ]
        ):
            print(line[:500])

    browser.close()
