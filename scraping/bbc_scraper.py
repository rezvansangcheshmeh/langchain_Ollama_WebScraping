import requests
from bs4 import BeautifulSoup

def scrape_bbc_titles():
    url = "https://www.bbc.com/news"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.find_all("h2")
    news_data = []
    for article in articles:
        title = article.get_text().strip()
        link_tag = article.find_parent("a")
        link = "https://www.bbc.com" + link_tag["href"] if link_tag and link_tag.get("href") else None
        if title and link:
            news_data.append((title, link))
    return news_data
