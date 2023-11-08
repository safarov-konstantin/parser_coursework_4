import npyscreen
from view.data_forms import data_forms
from works_api.hh_api import HeadHunterAPI
from utils.json_saver import JSONSaver
from utils.vacancy import Vacancy


class VacancyForm_HH(npyscreen.Form):
    """
    Класс форма для отображения и выбора вакансий с hh.ru
    последующим сохранением в json файл
    """
    def beforeEditing(self):
        
        params = {
            'text': f'NAME:{data_forms["selected_text"]}',  # Текст фильтра. В имени должно быть слово "Аналитик"
            'area': 1,  # Поиск ощуществляется по вакансиям города Москва
            'page': 0,  # Индекс страницы поиска на HH
            'per_page': 10,  # Кол-во вакансий на 1 странице
            'salary': data_forms['selected_salary'],
            'experience': data_forms['selected_experience_id'],
            'only_with_salary': True
        }
        
        hh_api = HeadHunterAPI()
        hh_vacancies = Vacancy.get_vacancy_hh_api(hh_api.get_vacancies(params))

        self.vacancies.values = []
        self.vacancies.value = []

        for vacancy_hh in hh_vacancies:
            self.vacancies.values.append(vacancy_hh)

    def afterEditing(self):
        json_saver = JSONSaver()
        a =  self.vacancies.value
        for i in self.vacancies.value:
            json_saver.add_vacancy(self.vacancies.values[i])
        json_saver.save_vacancies()
        self.parentApp.setNextForm('MAIN')    
        
    def create(self):   
       self.vacancies = self.add(       
            npyscreen.TitleMultiSelect, 
            scroll_exit=True, 
            # max_height=0,          
            name='Вакансии',
            values = [],
       )