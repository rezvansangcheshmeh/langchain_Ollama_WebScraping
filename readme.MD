
# 📰 BBC News Scraper & NLP Analyzer

This project is a complete pipeline for scraping, analyzing, and summarizing news articles from the BBC website. It uses modern web scraping tools and natural language processing models to extract structured data and store it in a PostgreSQL database.

---

## 🚀 Features

- Scrapes headlines and article links from BBC News
- Uses a language model to extract keywords and classify topics
- Retrieves full article content using Playwright
- Summarizes articles in 3 concise lines
- Stores all data in a PostgreSQL database

---

## 🧠 Technologies Used

| Tool / Library             | Purpose                                      |
|---------------------------|----------------------------------------------|
| `LangChain` + `Ollama`    | Keyword extraction and summarization         |
| `Playwright`              | Headless browser for article content scraping|
| `BeautifulSoup`           | HTML parsing for headline extraction         |
| `psycopg2`                | PostgreSQL database connection               |
| `python-dotenv`           | Environment variable management              |
| `asyncio`                 | Asynchronous execution for Playwright        |

---

## 📁 Project Structure

news_scraper_project/ 

├── main.py # Entry point 

├── config.py # Environment-based configuration 

├── database/ 
│ └── db_handler.py # DB connection and storage logic 

├── scraping/ │ └── bbc_scraper.py # BBC headline scraper 

├── nlp/ │ ├── analyzer.py # Keyword extraction and classification 

│ └── summarizer.py # Article summarization 

├── browser/ │ └── playwright_handler.py # Article content retrieval 

└── utils/ └── helpers.py # Utility functions


---

## ⚙️ Setup Instructions

1. **Install dependencies**:

```bash
pip install -r requirements.txt
Create a .env file in the root directory:

env
DB_NAME=web_psql_nlp
DB_USER=postgres
DB_PASSWORD=your_password_here
DB_HOST=localhost
DB_PORT=5432
Run the project:

bash
python main.py
📊 Sample Output
## 📊 Sample Output

| Title                                                                 | Link                                                              | Keywords                                             | Category                | Summary                                                   |
|-----------------------------------------------------------------------|-------------------------------------------------------------------|------------------------------------------------------|-------------------------|------------------------------------------------------------|
| Ukraine's European allies say peace talks must include Kyiv          | [Link](https://www.bbc.com/news/articles/c0e9py7e28xo)            | Ukraine, peace talks, Kyiv, allies, European         | International Politics  | European allies have called for Ukraine to be included... |
| Mars rock found in Niger sells for millions in New York              | [Link](https://www.bbc.com/news/articles/cly3q635n4no)            | Mars rock, Niger, New York, Millions, Answers        | Science and Technology  | A large meteorite believed to be from Mars was sold...     |
| Mohamed Salah calls out Uefa over wording of Palestinian tribute     | [Link](https://www.bbc.com/sport/football/articles/ckgl6re9922o)  | Mohamed Salah, Uefa, Palestinian player, tribute     | Sports & Politics       | Mohamed Salah criticized UEFA for not mentioning...        |


🛡️ Notes
Do not commit your .env file to version control.

Ensure Ollama is installed and running locally for language model access.

Use the synchronous version of Playwright on Windows for compatibility.



