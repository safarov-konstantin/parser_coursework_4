import npyscreen
from view.search_sys_form import SearchSysForm
from view.filter_form_hh import FilterForm_HH
from view.vacancy_form_hh import VacancyForm_HH
from view.filter_from_sperjob import FilterForm_SuperJob
from view.vacancy_from_superjob import VacancyFormSuperJob
from view.filter_saved_forms import FilterFormSaved
from view.vacancy_saved_forms import VacancyFormSaved

class MyApplication(npyscreen.NPSAppManaged):
   """
   Класс для иницилицации всех искользуемых форм
   """
   def onStart(self):
       self.addForm('MAIN', SearchSysForm, name='Выберите реусурс для поиска вакансии')
       self.addForm('FILTER_HH', FilterForm_HH, name='Параметры поиска hh.ru')
       self.addForm('VACANCY_HH', VacancyForm_HH, name='Вакансии по выбранным параметрам на hh.ru')
       self.addForm('FILTER_SUPERJOB', FilterForm_SuperJob, name='Параметры поиска superjob.ru')
       self.addForm('VACANCY_SUPERJOB', VacancyFormSuperJob, name='Вакансии по выбранным параметрам на superjob.ru')
       self.addForm('FILTER_SAVED', FilterFormSaved, name='Параметры сортировки сохраненных')
       self.addForm('VACANCY_SAVED', VacancyFormSaved, name='Сохраненные вакансии')
       # A real application might define more forms here.......