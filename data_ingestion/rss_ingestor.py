import feedparser

def fetch_rss_feeds(feed_urls):
    news_items = []
    for url in feed_urls:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            news_items.append({
                "title": entry.title,
                "link": entry.link,
                "summary": entry.summary,
                "published": entry.published
            })
    return news_items
