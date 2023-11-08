import json
import os
from utils.vacancy import Vacancy
from pathlib import Path


class JSONSaver:
    """
    Класс для работы с json файлами
    """
    saver_vacancies = []
    path_file = os.path.join(Path(__file__).parent.parent, 'data/data_vacancies.json')

    def __init__(self):
        self.saver_vacancies = self.__fill_in_saver_vacancies_JSON()

    def add_vacancy(self, vacancy):
        for saver_vacancy in self.saver_vacancies:
            if saver_vacancy == vacancy:
                return None
        self.saver_vacancies.append(vacancy)

    def save_vacancies(self):
        with open(self.path_file, 'w', encoding='utf8') as file:
            file.write(self.__saver_vacancies_to_JSON())

    def __saver_vacancies_to_JSON(self):
        saver_vacancies_json = []
        for saver_vacancy in self.saver_vacancies:
            dump = {'name': saver_vacancy.name,
                    'url': saver_vacancy.url,
                    'experience': saver_vacancy.experience,
                    'salary': saver_vacancy.salary}
            saver_vacancies_json.append(dump)
        return json.dumps(saver_vacancies_json)

    def __fill_in_saver_vacancies_JSON(self):
        try:
            with open(self.path_file, 'r', encoding='utf8') as file:
                saver_vacancies_json = json.loads(file.read())
            saver_vacancies = [Vacancy(**i) for i in saver_vacancies_json]
            return saver_vacancies
        except:
            return []