from lab_1.HTML_crawler.html_crawler import get_html_page, find_articles, publish_report
import datetime
import requests as client

url = 'https://journal.tinkoff.ru/selected/around-the-world/'
html_page = get_html_page(client, url).text
articles = find_articles(html_page)
creation_date = datetime.datetime.now().strftime("%Y-%m-%d")
summary = {"url": url,
           "creationDate": creation_date,
           "articles": articles}

path = "articles.json"
publish_report(path, summary)
