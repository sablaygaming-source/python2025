import requests
from bs4 import BeautifulSoup
import csv
import time

# =============================
# CONFIG
# =============================
URL = "https://quotes.toscrape.com/"
HEADERS = {
    "User-Agent": "Mozilla/5.0"
}
OUTPUT_FILE = "quotes.csv"

# =============================
# FETCH PAGE
# =============================
def fetch_page(url):
    response = requests.get(url, headers=HEADERS, timeout=10)
    response.raise_for_status()  # raise error if request fails
    return response.text

# =============================
# PARSE DATA
# =============================
def parse_quotes(html):
    soup = BeautifulSoup(html, "lxml")
    quotes_data = []

    quotes = soup.find_all("div", class_="quote")

    for q in quotes:
        text = q.find("span", class_="text").get_text(strip=True)
        author = q.find("small", class_="author").get_text(strip=True)

        quotes_data.append({
            "quote": text,
            "author": author
        })

    return quotes_data

# =============================
# SAVE TO CSV
# =============================
def save_to_csv(data, filename):
    with open(filename, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=["quote", "author"])
        writer.writeheader()
        writer.writerows(data)


# =============================
# MAIN
# =============================
def main():
    print("Fetching page...")
    html = fetch_page(URL)

    print("Parsing quotes...")
    quotes = parse_quotes(html)

    a, b = zip(*quotes[0].items())


    sample = "result"
    print(f"\ndebug {sample} {repr(b[0])}")

    print(f"Saving {len(quotes)} quotes...")
    save_to_csv(quotes, OUTPUT_FILE)

    print("Done!")

if __name__ == "__main__":
    main()


"""
#additional code for multilple
page = 1
all_quotes = []

while True:
    url = f"https://quotes.toscrape.com/page/{page}/"
    html = fetch_page(url)
    quotes = parse_quotes(html)

    if not quotes:
        break

    all_quotes.extend(quotes)
    page += 1
    time.sleep(1)  # be polite

save_to_csv(all_quotes, "all_quotes.csv")


"""



