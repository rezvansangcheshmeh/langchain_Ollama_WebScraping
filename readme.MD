markdown
# 📰 BBC News Scraper & NLP Analyzer

This project is a complete pipeline for scraping, analyzing, and summarizing news articles from the BBC website. It uses modern web scraping tools and natural language processing models to extract structured data and store it in a PostgreSQL database.

---

## ⚙️ Setup Instructions

### 1. Install dependencies

```bash
pip install -r requirements.txt
2. Create a .env file in the root directory
env
DB_NAME=web_psql_nlp
DB_USER=postgres
DB_PASSWORD=your_password_here
DB_HOST=localhost
DB_PORT=5432
3. Run the project
bash
python main.py
📊 Sample Output
Here is a sample of the structured data stored in the database:

Title	Link	Keywords	Category	Summary
Ukraine's European allies say peace talks must include Kyiv	Link	Ukraine, peace talks, Kyiv, allies, European	International Politics	European allies have called for Ukraine to be included in any peace talks with Russia...
Mars rock found in Niger sells for millions in New York	Link	Mars rock, Niger, New York, Millions, Answers	Science and Technology	A large meteorite believed to be from Mars was sold by Sotheby's auction house...
Mohamed Salah calls out Uefa over wording of Palestinian tribute	Link	Mohamed Salah, Uefa, Palestinian player, tribute	Sports & Politics	Mohamed Salah criticized UEFA for not mentioning the circumstances surrounding the tribute...
🛡️ Notes
Do not commit your .env file to version control. Add it to .gitignore.

Make sure Ollama is installed and running locally to enable language model access.

On Windows, use the synchronous version of Playwright to avoid compatibility issues with asyncio.
