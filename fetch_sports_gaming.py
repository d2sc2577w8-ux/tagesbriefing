import json
import feedparser
from datetime import datetime, timezone

SPORT_FEEDS = [
    "https://www.srf.ch/sport/bnf/rss/718",   # SRF Sport allgemein
    "https://www.srf.ch/sport/bnf/rss/2562",  # SRF Fussball
]

GAMING_FEEDS = [
    "https://www.pcgames.de/feed/",
]

def fetch_feed(url, limit=6):
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
    sport_news = []
    for url in SPORT_FEEDS:
        sport_news.extend(fetch_feed(url, limit=6))

    gaming_news = []
    for url in GAMING_FEEDS:
        gaming_news.extend(fetch_feed(url, limit=6))

    result = {
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "sport": sport_news,
        "gaming": gaming_news,
    }

    with open("sports_gaming.json", "w") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"Gespeichert: {len(sport_news)} Sport, {len(gaming_news)} Gaming")

if __name__ == "__main__":
    main()
