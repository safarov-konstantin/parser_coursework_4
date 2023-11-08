import npyscreen
from view.data_forms import data_forms
from works_api.superjob import SuperJobAPI
from utils.json_saver import JSONSaver
from utils.vacancy import Vacancy


class VacancyFormSuperJob(npyscreen.Form):
    """
    Класс форма для отображения и выбора вакансий с superjob.ru
    последующим сохранением в json файл
    """
    def beforeEditing(self):
        
        params = {
            'keyword': data_forms["selected_text"], 
            'count': 10, 
            'page': 0, 
            'payment_from': data_forms['selected_salary'],
            'town': 'Москва', 
            'experience': data_forms['selected_experience_id']
        }

        superjob_api = SuperJobAPI()
        data_superjob_api = superjob_api.get_vacancies(params)
        superjob_vacancies = Vacancy.get_vacancy_superjob_api(data_superjob_api)

        self.vacancies.values = []
        self.vacancies.value = []

        for vacancy_superjob in superjob_vacancies:
            self.vacancies.values.append(vacancy_superjob)

    def afterEditing(self):
        json_saver = JSONSaver()
        for i in self.vacancies.value:
            json_saver.add_vacancy(self.vacancies.values[i])
        json_saver.save_vacancies()
        self.parentApp.setNextForm('MAIN')    
        
    def create(self):   
       self.vacancies = self.add(       
            npyscreen.TitleMultiSelect, 
            scroll_exit=True,           
            name='Вакансии',
            values = [],
       )