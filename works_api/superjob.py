import requests, json, os
from works_api.client_api import ApiClient


class SuperJobAPI(ApiClient):
    """
    Класс для работы с API HeadHunter
    """
    url_vacancies = 'https://api.superjob.ru/2.0/vacancies/'
    url_dictionaries = 'https://api.superjob.ru/2.0/references/'
    header = None

    def __init__(self):
        api_key = os.getenv('API_KEY_SJ')
        self.header = {'X-Api-App-Id': api_key} 

    def get_vacancies(self, params):
        
        req = requests.get(SuperJobAPI.url_vacancies, headers=self.header, params=params) 
        data = req.content.decode()  
        req.close()
        data = json.loads(data)

        return data['objects']
    
    @staticmethod
    def get_solary_representation(payment_from, payment_to, currency): 

        if currency == 'rub':
            salary_currency = 'руб.'

        if payment_from is None and payment_to is None:
            return 'Не указана'
        elif (payment_from is not None) and (payment_to is not None):
            return f"{payment_from} - {payment_to} {salary_currency}"
        elif (payment_from is not None) and (payment_to is None):
            return f"{payment_from} {salary_currency}"
        elif (payment_from is None) and (payment_to is not None):
            return f"до {payment_to} {salary_currency}"

    @staticmethod
    def get_dictionaries():
        req = requests.get(SuperJobAPI.url_dictionaries, headers=SuperJobAPI.header)  
        data = req.content.decode()  
        req.close()
        return json.loads(data) 