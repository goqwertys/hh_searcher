import json

from src.vacancy import Vacancy
from src.vacancy_saver import VacancySaver


class JSONSaver(VacancySaver):
    def __init__(self):
        pass

    def add_vacancy(self, vacancy: Vacancy):
        pass

    def get_vacancies(self):
        pass

    def delete_vacancy(self, vacancy: Vacancy):
        pass
