import npyscreen
from view.data_forms import data_forms

class SearchSysForm(npyscreen.ActionForm):
    """
    Класс форма для выбора поисковой системы и 
    сохраненных данных об вакансиях
    """
    def beforeEditing(self):
        data_forms['search_system'] = None
        data_forms['experience_hh'] = None
        data_forms['selected_experience_id'] = None
        data_forms['selected_text'] = None
        data_forms['selected_salary'] = None        

    def create(self):   
       self.search_system = self.add(       
            npyscreen.TitleSelectOne, 
            scroll_exit=True, 
            # max_height=0,          
            name='Выберите систему поиска вакансий',
            values = ['hh.ru', 'superjob.ru', 'Сохраненные'],
            value = [0]
       )

    # переопределенный метод, срабатывающий при нажатии на кнопку «cancel»
    def on_cancel(self):
        self.parentApp.setNextForm(None)

    def on_ok(self):
        data_forms['search_system'] = self.search_system.values[self.search_system.value[0]]
        if data_forms['search_system'] == 'hh.ru':  
            self.parentApp.setNextForm('FILTER_HH')
        elif data_forms['search_system'] == 'superjob.ru':  
            self.parentApp.setNextForm('FILTER_SUPERJOB')    
        elif data_forms['search_system'] == 'Сохраненные':
            self.parentApp.setNextForm('FILTER_SAVED')
        else:
            self.parentApp.setNextForm(None) 