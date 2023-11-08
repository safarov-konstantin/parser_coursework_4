import requests
import json
from works_api.client_api import ApiClient


class HeadHunterAPI(ApiClient):
    """
    Класс для работы с API HeadHunter
    """

    url_vacancies = 'https://api.hh.ru/vacancies'
    url_dictionaries = 'https://api.hh.ru/dictionaries'

    def get_vacancies(self, params):

        req = requests.get(HeadHunterAPI.url_vacancies, params)  # Посылаем запрос к API
        data = req.content.decode()  # Декодируем его ответ, чтобы Кириллица отображалась корректно
        req.close()
        data = json.loads(data)

        return data['items']

    @staticmethod
    def get_solary_representation(salary_hh):
        if salary_hh is None:
            return 'Не указана'

        salary_from = salary_hh['from']
        salary_to = salary_hh['to']
        salary_currency = salary_hh['currency']

        if salary_currency == 'RUR':
            salary_currency = 'руб.'

        if salary_from is None and salary_to is None:
            return 'Не указана'
        elif (salary_from is not None) and (salary_to is not None):
            return f"{salary_from} - {salary_to} {salary_currency}"
        elif (salary_from is not None) and (salary_to is None):
            return f"{salary_from} {salary_currency}"
        elif (salary_from is None) and (salary_to is not None):
            return f"до {salary_to} {salary_currency}"

    @staticmethod
    def get_dictionaries_hh():
        req = requests.get('https://api.hh.ru/dictionaries')  
        # Декодируем его ответ, чтобы Кириллица отображалась корректно
        data = req.content.decode()  
        req.close()
        return json.loads(data)        