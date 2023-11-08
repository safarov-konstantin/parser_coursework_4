from abc import ABC, abstractmethod


class ApiClient(ABC):
    """Класс для получения вакансий с помощью API"""
    @abstractmethod
    def get_vacancies(self, params):
        pass