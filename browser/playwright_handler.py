from playwright.sync_api import sync_playwright

def get_article_text(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        try:
            content = page.locator("article").inner_text()
        except:
            content = ""
        browser.close()
        return content
