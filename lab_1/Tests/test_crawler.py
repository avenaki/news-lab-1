import datetime
import unittest
import json
import validators
from lab_1.HTML_crawler.html_crawler import get_html_page, find_articles, publish_report



class TestCrawler(unittest.TestCase):
    def setUp(self):
        test_page_file = open("lab_1/Tests/news_test_page.html", "r", encoding="UTF-8")
        test_page_content = test_page_file.read()
        test_page_file.close()
        self.url = 'https://journal.tinkoff.ru/selected/around-the-world/'
        self.html = test_page_content
        self.control_array = [{'title': 'На автомобиле в Грузию и Армению'},
                              {'title': 'Двухнедельное путешествие в Коста-Рику'},
                              {'title': 'Поездка в Бразилию'}, {'title': 'Самостоятельное путешествие по Кубе'},
                              {'title': 'Отдых на Крите'},
                              {'title': 'По Норвегии за 7000 рублей'},
                              {'title': 'На машине по Казахстану, Киргизии и Узбекистану'},
                              {'title': 'Экономная поездка в Париж'}, {'title': 'Путешествие по Каталонии'},
                              {'title': 'На поезде по Бельгии'},
                              {'title': 'Автопутешествие по Исландии'}, {'title': 'Отпуск в Дагестане'},
                              {'title': 'Экономное путешествие в Нью-Йорк'},
                              {'title': 'Кругосветное путешествие'}, {'title': 'Путешествие в Танзанию'},
                              {'title': 'Трекинг в Непале'},
                              {'title': 'Автопутешествие по Польше за 20 000 ₽'}, {'title': 'Бомж-трип во Францию'},
                              {'title': 'Отдых в Грузии'}, {'title': 'Поездка в Перу'}, {'title': 'Марокко за 9 дней'},
                              {'title': 'Отдых в Абхазии'}, {'title': 'Пешком по «Пути Сантьяго» в Испании'},
                              {'title': 'По Италии на поездах'}, {'title': 'По Шотландии на автомобиле'},
                              {'title': 'Дешево отдохнуть в Карелии'}, {'title': 'По Испании на трамвае'},
                              {'title': 'По Греции на паромах'}, {'title': 'Две недели в Японии'},
                              {'title': 'На Новый год в Финляндию'},
                              {'title': 'Поездка в Абхазию зимой'}, {'title': 'Отпуск в Нидерландах'},
                              {'title': 'Отдохнуть на Бали'},
                              {'title': 'Как не потерять деньги на Бали'}, {'title': 'По США на автобусах'},
                              {'title': 'На шопинг в Милан'},
                              {'title': 'Кататься в Красной поляне'}, {'title': 'Перезимовать в Египте'},
                              {'title': 'С гидом по Израилю'},
                              {'title': 'Объехать Пхукет на машине'}, {'title': 'В Европу волонтером'},
                              {'title': 'Объехать Австралию'},
                              {'title': 'Без денег в Сингапуре'}, {'title': 'Отпуск на Мадейре'},
                              {'title': 'Проехать по Золотому кольцу'},
                              {'title': 'Перезимовать в Индии'}, {'title': 'Что посмотреть на Байкале'},
                              {'title': 'Жить полгода в Мексике'},
                              {'title': 'Съездить на полуостров Святой Нос'}]

    def test_find_articles(self):
        self.assertListEqual(find_articles(self.html), self.control_array)

    def test_get_html_page(self):
        self.assertEqual(get_html_page(self.url).status_code, 200)

    def test_file_structure(self):
        creation_date = datetime.datetime.now().strftime("%Y-%m-%d")
        summary = {"url": self.url,
                   "creationDate": creation_date,
                   "articles": self.control_array}
        path = "lab_1/Tests/test_articles.json"
        publish_report(path, summary)
        with open(path, 'r', encoding="UTF-8") as articles_data:
            data = json.load(articles_data)
        self.assertTrue(validators.url(data["url"]))
        try:
            creation_date_datetime = datetime.datetime.strptime(data["creationDate"], '%Y-%m-%d').date()
        except ValueError:
            print('Invalid date!')
        self.assertNotEqual(len(data["articles"]), 0)

    if __name__ == '__main__':
        unittest.main()
