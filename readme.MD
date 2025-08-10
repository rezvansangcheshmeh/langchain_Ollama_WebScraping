# 📰 BBC News Scraper & NLP Analyzer

This project is a complete pipeline for scraping, analyzing, and summarizing news articles from the BBC website. It uses modern web scraping tools and natural language processing models to extract structured data and store it in a PostgreSQL database.

---

## ⚙️ Setup Instructions

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2.Create a .env file in the root directory

```env
DB_NAME=web_psql_nlp
DB_USER=postgres
DB_PASSWORD=your_password_here
DB_HOST=localhost
DB_PORT=5432
```
### 3.Run the project
```bash
python main.py
```

---
📊 Sample Output
Instead of using a cluttered table, here’s a clean and readable format for sample entries stored in the database:

```markdown
📰 1. Ukraine's European allies say peace talks must include Kyiv
Link: View Article Keywords: Ukraine, peace talks, Kyiv, allies, European Category: International Politics Summary: European allies have called for Ukraine to be included in any peace talks with Russia...

🪐 2. Mars rock found in Niger sells for millions in New York
Link: View Article Keywords: Mars rock, Niger, New York, Millions, Answers Category: Science and Technology Summary: A large meteorite believed to be from Mars was sold by Sotheby's auction house...

⚽ 3. Mohamed Salah calls out Uefa over wording of Palestinian tribute
Link: View Article Keywords: Mohamed Salah, Uefa, Palestinian player, tribute Category: Sports & Politics Summary: Mohamed Salah criticized UEFA for not mentioning the circumstances surrounding the tribute...

```


