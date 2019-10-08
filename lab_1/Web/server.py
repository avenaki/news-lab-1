from lab_1.HTML_crawler.html_crawler import get_html_page, find_articles, publish_report
import datetime
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def run_crawler():
    url = 'https://journal.tinkoff.ru/selected/around-the-world/'
    html_page = get_html_page(url).text
    articles = find_articles(html_page)
    creation_date = datetime.datetime.now().strftime("%Y-%m-%d")
    summary = {"url": url,
               "creationDate": creation_date,
               "articles": articles}
    path = "../HTML_crawler/articles.json"
    publish_report(path, summary)
    return render_template('news_page.html', url=url, date=creation_date, articles=articles)


if __name__ == '__main__':
    app.run(host='localhost', port=8000)
