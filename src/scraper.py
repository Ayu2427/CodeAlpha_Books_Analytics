import time
from pathlib import Path
import requests
import pandas as pd
from bs4 import BeautifulSoup

BASE_URL = "https://books.toscrape.com/"
OUTPUT = Path("data/books_scraped.csv")
HEADERS = {"User-Agent": "Mozilla/5.0 (educational web scraping project)"}

def scrape_page(url):
    response = requests.get(url, headers=HEADERS, timeout=20)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    rows = []
    for card in soup.select("article.product_pod"):
        title = card.select_one("h3 a")
        price = card.select_one("p.price_color")
        stock = card.select_one("p.instock.availability")
        rating = card.select_one("p.star-rating")
        href = title.get("href", "") if title else ""
        rows.append({
            "Title": title.get("title", "").strip() if title else "",
            "Price": price.get_text(strip=True) if price else "",
            "Availability": stock.get_text(" ", strip=True) if stock else "",
            "Rating": rating.get("class", ["", "Unknown"])[1] if rating and len(rating.get("class", [])) > 1 else "Unknown",
            "URL": BASE_URL + "catalogue/" + href.replace("../", "") if href else ""
        })
    return rows, soup

def main():
    all_rows, url, page = [], BASE_URL, 1
    while url:
        print(f"Scraping page {page}: {url}")
        rows, soup = scrape_page(url)
        all_rows.extend(rows)
        next_link = soup.select_one("li.next a")
        if not next_link:
            break
        url = BASE_URL + "catalogue/" + next_link["href"]
        page += 1
        time.sleep(0.5)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(all_rows).to_csv(OUTPUT, index=False, encoding="utf-8-sig")
    print(f"Saved {len(all_rows)} records to {OUTPUT}")

if __name__ == "__main__":
    main()
