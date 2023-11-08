import npyscreen
from view.data_forms import data_forms
from works_api.superjob import SuperJobAPI


class FilterForm_SuperJob(npyscreen.Form):
    """
    Класс формы для работы с фильтрами superjob.ru
    """
    def beforeEditing(self):
            dictionaries = SuperJobAPI.get_dictionaries()
            data_forms['experience_hh'] = dictionaries['experience']
            self.experience.values = [i for i in dictionaries['experience'].values()]
    
    def afterEditing(self):
        # заполняем selected_experience_id по выбранным значениям пользователя 
        if len(self.experience.value) != 0:
            a = str(self.experience.value[0])
            data_forms['selected_experience_id'] = str(self.experience.value[0])
             
        # заполняем selected_text по выбранным значениям пользователя
        if self.search_string.value != '':          
            data_forms['selected_text'] = self.search_string.value
        
        # заполняем selected_salary по выбранным значениям пользователя
        try:
            data_forms['selected_salary'] = int(self.search_salary.value.replace(' ', ''))
        except ValueError:
            pass 

        # Проверяем на заполнение введенных данных от пользователя
        if (data_forms['selected_experience_id'] is None 
                or data_forms['selected_text'] is None
                or data_forms['selected_salary'] is None):
            self.error.value = 'Для продолжения нужно заполнить все параметры для поиска!!!'        
        else:
            # Очищаем значения введенные пользователем
            self.experience.value = []
            self.search_string.value = ''
            self.search_salary.value = '' 
            # Переходим на форму найденных вакансий hh.ru
            self.parentApp.setNextForm('VACANCY_SUPERJOB')

    def create(self):
       self.description = self.add(npyscreen.MultiLineEdit, 
                                   value=FilterForm_SuperJob.get_form_description(),
                                   max_height=7)
       
       self.search_string = self.add(npyscreen.TitleText, name='Професия: ')
       self.search_salary = self.add(npyscreen.TitleText, name='Зарплата от: ')
       self.experience = self.add(
           npyscreen.TitleSelectOne, 
           scroll_exit=True, 
           max_height=4, 
           name='Опыт',
           values = []
        )
       self.error = self.add(npyscreen.MultiLineEdit, max_height=5, rely = 15)   

    def get_form_description():
        form_description = ('Форма для выбора параметров поиска superjob.ru\n'
                            + '\t\tПрофессия - профессия, должность для поиска\n'
                            + '\t\tЗарплата от - будет произведен поиск вакансий начиная с этой суммы\n'
                            + '\t\tОпыт - опыт требуемый работадателем\n\n'
                            + 'ВСЕ ПАРАМЕТРЫ ПОИСКА ДОЛЖНЫ БЫТЬ ЗАПОЛНЕНЫ!!!\n')

        return form_description