import unittest
from bs4 import BeautifulSoup
from html_crawler import get_html_page, find_articles


class TestCrawler(unittest.TestCase):
    # def test_html_page(self): #проверяем структуру файла: url, список статей с хотя бы 1 элементом
    #   with open('html_test_page.txt') as f:
    #      soup = BeautifulSoup(f, "html.parser")

    def setUp(self):
        self.control_array = ['На автомобиле в Грузию и Армению', 'Двухнедельное путешествие в Коста-Рику',
                         'Поездка в Бразилию', 'Самостоятельное путешествие по Кубе', 'Отдых на Крите',
                         'По Норвегии за 7000 рублей', 'На машине по Казахстану, Киргизии и Узбекистану',
                         'Экономная поездка в Париж', 'Путешествие по Каталонии', 'На поезде по Бельгии',
                         'Автопутешествие по Исландии', 'Отпуск в Дагестане', 'Экономное путешествие в Нью-Йорк',
                         'Кругосветное путешествие', 'Путешествие в Танзанию', 'Трекинг в Непале',
                         'Автопутешествие по Польше за 20 000 ₽', 'Бомж-трип во Францию', 'Отдых в Грузии',
                         'Поездка в Перу', 'Марокко за 9 дней', 'Отдых в Абхазии',
                         'Пешком по «Пути Сантьяго» в Испании',
                         'По Италии на поездах', 'По Шотландии на автомобиле', 'Дешево отдохнуть в Карелии',
                         'По Испании на трамвае', 'По Греции на паромах', 'Две недели в Японии',
                         'На Новый год в Финляндию',
                         'Поездка в Абхазию зимой', 'Отпуск в Нидерландах', 'Отдохнуть на Бали',
                         'Как не потерять деньги на Бали',
                         'По США на автобусах', 'На шопинг в Милан', 'Кататься в Красной поляне',
                         'Перезимовать в Египте',
                         'С гидом по Израилю', 'Объехать Пхукет на машине', 'В Европу волонтером', 'Объехать Австралию',
                         'Без денег в Сингапуре', 'Отпуск на Мадейре', 'Проехать по Золотому кольцу',
                         'Перезимовать в Индии',
                         'Что посмотреть на Байкале', 'Жить полгода в Мексике', 'Съездить на полуостров Святой Нос']

    def test_find_articles(self):
        self.assertListEqual(find_articles(), self.control_array)
