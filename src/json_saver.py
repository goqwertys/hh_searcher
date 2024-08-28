import json

from isort.profiles import attrs

from src.vacancy import Vacancy
from src.vacancy_saver import VacancySaver


class JSONSaver(VacancySaver):
    def __init__(self, filename: str):
        self.filename = filename

    def add_vacancy(self, vacancy: Vacancy):
        """ Adds vacancy to file """
        with open(self.filename, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # using getattr bc Vacancy described with __slots__
        vacancy_dict = {attr: getattr(vacancy, attr) for attr in vacancy.__slots__}
        data.append(vacancy_dict)

        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def get_vacancies(self):
        pass

    def delete_vacancy(self, vacancy: Vacancy):
        pass
