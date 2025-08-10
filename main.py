from scraping.bbc_scraper import scrape_bbc_titles
from browser.playwright_handler import get_article_text
from nlp.analyzer import analyze_news
from nlp.summarizer import summarize_article
from database.db_handler import save_news_item

def run():
    news_items = scrape_bbc_titles()
    news_items = news_items[0:2]
    for title, link in news_items:
        keywords, category = analyze_news(title)
        try:
            article_text = get_article_text(link)
            summary = summarize_article(article_text)
        except Exception as e:
            summary = ""
        save_news_item(title, link, keywords, category, summary)

if __name__ == "__main__":
    run()
