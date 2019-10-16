import json
import io
from bs4 import BeautifulSoup
import requests


def get_html_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response
    else:
        return "HTML is not valid"


def find_articles(html_page):
    parsed_page = BeautifulSoup(html_page, 'html.parser')
    parsed_page = parsed_page.find_all('h2')
    headers = [header.get_text() for header in parsed_page]
    articles = [{"title": header} for header in headers]
    return articles


def publish_report(path, summary):
    with io.open(path, 'w', encoding='utf8') as json_file:
        json.dump(summary, json_file, ensure_ascii=False)
