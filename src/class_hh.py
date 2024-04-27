import requests
import json

class HH():

    def __init__(self, url):
        self.url = url
        self.params = {'text': '', 'page': 0, 'per_page': 100, 'area': 113, "only_with_vacancies": True}


    def get_data(self, id) -> list:
        ''' Получает данные из апи hh.ru по необходимым компаниям (используя их id) '''
        url = f'{self.url}{id}'
        response = requests.get(url, params=self.params)
        data = response.json()['items']
        return data

class JSONSaver():

    def __init__(self, file):
        self.file = file

    def write_file(self, data) -> None:
        ''' Записывает и добавляет данные в файл '''
        with open(self.file, 'a', encoding='utf-8') as new_file:
            json.dump(data, new_file, indent=4, ensure_ascii=False)

