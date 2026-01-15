# lib/GetRequester.py

from urllib.request import urlopen
import json
import ssl


class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        context = ssl._create_unverified_context()

        with urlopen(self.url, context=context) as response:
            return response.read()  

    def load_json(self):
        response_body = self.get_response_body()
        return json.loads(response_body.decode("utf-8"))
