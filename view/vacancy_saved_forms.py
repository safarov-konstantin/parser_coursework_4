import npyscreen
from view.data_forms import data_forms
from utils.json_saver import JSONSaver


class VacancyFormSaved(npyscreen.ActionForm):
    """
    Класс форма для отображения и выбора вакансий с 
    сохраненными вакансиями, с возможностью уделения 
    из файла json
    """
    def beforeEditing(self):
        self.vacancies.value = []
        self.CANCEL_BUTTON_TEXT = 'Удалить выбранные'
        self.saver_json = JSONSaver()
        vacancies_saved = self.saver_json.saver_vacancies
        self.vacancies.values = []
        self.vacancies.value = []
        sort_by = data_forms['sort_by']
        if sort_by is not None:
            vacancies_saved.sort(key=lambda x: getattr(x, sort_by)) 

        for vacancy_hh in vacancies_saved:
            self.vacancies.values.append(vacancy_hh)   
    
    def create(self):   
       self.vacancies = self.add(       
            npyscreen.TitleMultiSelect, 
            scroll_exit=True,
            name='Вакансии',           
            values = [],
       )

    def on_cancel(self):
        vacancies_saved = self.saver_json.saver_vacancies
        if len(self.vacancies.value) != 0:
            index_del = self.vacancies.value[:]
            index_del.sort(reverse=True)
            for i in index_del:
                vacancies_saved.pop(i)
        self.saver_json.save_vacancies()        
        self.parentApp.setNextForm('VACANCY_SAVED')   

    def on_ok(self):
        self.parentApp.setNextForm('MAIN')    