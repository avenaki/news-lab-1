class testclient:
    def get(self, url):
        test_page_file = open("../Tests/news_test_page.html", "r", encoding="UTF-8")
        page_content = test_page_file.read()
        test_page_file.close()
        if (url == 'https://journal.tinkoff.ru/selected/around-the-world/'):
            return page_content
