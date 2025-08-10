# 📰 BBC News Scraper & NLP Analyzer

This project is a complete pipeline for scraping, analyzing, and summarizing news articles from the BBC website. It uses modern web scraping tools and natural language processing models to extract structured data and store it in a PostgreSQL database.

---

## ⚙️ Setup Instructions

1. **Install dependencies**:

```bash
pip install -r requirements.txt

2.Create a .env file in the root directory with the following content:
DB_NAME=web_psql_nlp
DB_USER=postgres
DB_PASSWORD=your_password_here
DB_HOST=localhost
DB_PORT=5432

3.Run the project:
python main.py

---

## 📊 Sample Output

## 📊 Sample Output
#markdown

| Title                                                                 | Link                                                              | Keywords                                             | Category                | Summary                                                   |
|-----------------------------------------------------------------------|-------------------------------------------------------------------|------------------------------------------------------|-------------------------|------------------------------------------------------------|
| Ukraine's European allies say peace talks must include Kyiv          | [Link](https://www.bbc.com/news/articles/c0e9py7e28xo)            | Ukraine, peace talks, Kyiv, allies, European         | International Politics  | European allies have called for Ukraine to be included... |
| Mars rock found in Niger sells for millions in New York              | [Link](https://www.bbc.com/news/articles/cly3q635n4no)            | Mars rock, Niger, New York, Millions, Answers        | Science and Technology  | A large meteorite believed to be from Mars was sold...     |
| Mohamed Salah calls out Uefa over wording of Palestinian tribute     | [Link](https://www.bbc.com/sport/football/articles/ckgl6re9922o)  | Mohamed Salah, Uefa, Palestinian player, tribute     | Sports & Politics       | Mohamed Salah criticized UEFA for not mentioning...        |






