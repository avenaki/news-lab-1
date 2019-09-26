import requests
import json
import io
from bs4 import BeautifulSoup



def get_html_page(url): # должна быть валидным HTML
    page_request = requests.get(url)
    if(page_request):
        return page_request.text
    else:
        return "HTML is not valid"


def find_articles(html_page): #  возвращает массив заголовков
    parsed_page = BeautifulSoup(html_page, 'html.parser')
    parsed_page = parsed_page.find_all('h2')
    headers = [header.get_text() for header in parsed_page]
    articles = [{"title": header} for header in headers]
    return articles

def publish_report(path, summary): #сохраняет массив заголовков в виде JSON
    with io.open(path, 'w', encoding='utf8') as json_file:
        json.dump(summary, json_file, ensure_ascii=False)