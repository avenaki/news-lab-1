import html_crawler
import datetime
import json

url = 'https://journal.tinkoff.ru/selected/around-the-world/'
html_page = html_crawler.get_html_page(url)
articles = html_crawler.find_articles(html_page)
creation_date = datetime.datetime.now().strftime("%Y-%m-%d")
summary = {"url": url,
           "creationDate": creation_date,
           "articles": articles}

path = "articles.json"
html_crawler.publish_report(path, summary)