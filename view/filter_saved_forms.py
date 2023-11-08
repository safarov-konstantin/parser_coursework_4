import npyscreen
from view.data_forms import data_forms


class FilterFormSaved(npyscreen.Form):
    """
    Класс формы для работы с фильтрами 
    сохраненных вакансий
    """
    def afterEditing(self): 
        if len(self.sort_by.value) != 0:
            data_forms['sort_by'] = 'name'
            self.sort_by.value = []

        self.parentApp.setNextForm('VACANCY_SAVED')

    def create(self):
       self.description = self.add(npyscreen.MultiLineEdit, 
                                   value=FilterFormSaved.get_form_description(),
                                   max_height=7)
       self.sort_by = self.add(
           npyscreen.TitleSelectOne, 
           scroll_exit=True, 
           max_height=4, 
           name='Cортировать по:',
           values = ["Наименованию"]
        )
          

    def get_form_description():
        form_description = ('Форма для выбора параметров сортировки сохраненных вакансий\n'
                            + '\t\tНаименование вакансии - сортировать по наименованию\n')

        return form_description