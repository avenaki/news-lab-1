import requests


class ClientTest:
    def get(self, url):
        return requests.get(url).status_code
