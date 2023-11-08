from works_api.hh_api import HeadHunterAPI
from works_api.superjob import SuperJobAPI



class Vacancy:
    """
    Класс для хранения данных об вакансиях
    """
    def __init__(self, name, url, salary, experience):
        self.name = name
        self.url = url
        self.salary = salary
        self.experience = experience

    def __repr__(self):
        return f'Vacancy(name: {self.name}, url: {self.url}, salary: {self.salary}, experience: {self.experience})'

    def __str__(self):
        description_vacancy = f'{self.name} \ Зарплата: {self.salary} \ Опыт: {self.experience} \ url: {self.url}' 
        return description_vacancy

    def __eq__(self, other):
        if isinstance(other, Vacancy):
            return self.url ==other.url
        else:
            return False

    @classmethod
    def get_vacancy_hh_api(cls, hh_vacancies):
        vacancies = []
        for hh_vacancy in hh_vacancies:
            name = hh_vacancy['name']
            url = hh_vacancy['alternate_url']
            salary = HeadHunterAPI.get_solary_representation(hh_vacancy['salary'])
            experience = hh_vacancy['experience']['name']
            vacancies.append(cls(name, url, salary, experience))
        return vacancies
    
    @classmethod
    def get_vacancy_superjob_api(cls, superjob_vacancies):
        vacancies = []
        for superjob_vacancy in superjob_vacancies:
            name = superjob_vacancy['profession']
            url = superjob_vacancy['link']
            salary = SuperJobAPI.get_solary_representation(
                superjob_vacancy['payment_from'], 
                superjob_vacancy['payment_to'],
                superjob_vacancy['currency'])
            experience = superjob_vacancy['experience']['title']
            vacancies.append(cls(name, url, salary, experience))
        return vacancies