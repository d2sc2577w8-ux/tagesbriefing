import json
import feedparser
from datetime import datetime, timezone

# RSS-Feeds: Politik (Schweiz/International) und KI
POLITIK_FEEDS = [
    "https://www.srf.ch/news/bnf/rss/1890",   # SRF News Schweiz
    "https://www.tagesschau.de/xml/rss2",      # Tagesschau Deutschland
]

KI_FEEDS = [
    "https://the-decoder.de/feed/",
]

def fetch_feed(url, limit=5):
    feed = feedparser.parse(url)
    items = []
    for entry in feed.entries[:limit]:
        items.append({
            "title": entry.get("title", ""),
            "link": entry.get("link", ""),
            "published": entry.get("published", ""),
            "source": feed.feed.get("title", url),
        })
    return items

def main():
    politik_news = []
    for url in POLITIK_FEEDS:
        politik_news.extend(fetch_feed(url, limit=4))

    ki_news = []
    for url in KI_FEEDS:
        ki_news.extend(fetch_feed(url, limit=5))

    result = {
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "politik": politik_news,
        "ki": ki_news,
    }

    with open("news.json", "w") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"News gespeichert: {len(politik_news)} Politik, {len(ki_news)} KI")

if __name__ == "__main__":
    main()
