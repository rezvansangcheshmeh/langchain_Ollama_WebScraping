import psycopg2
from config import DB_CONFIG

def save_news_item(title, link, keywords, category, summary):
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS news (
            id SERIAL PRIMARY KEY,
            title TEXT,
            link TEXT,
            keywords TEXT,
            category TEXT,
            summary TEXT
        )
    """)
    cur.execute("""
        INSERT INTO news (title, link, keywords, category, summary)
        VALUES (%s, %s, %s, %s, %s)
    """, (title, link, ', '.join(keywords), category, summary))
    conn.commit()
    cur.close()
    conn.close()
