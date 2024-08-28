import json
from src.json_saver import JSONSaver

from src.vacancy import Vacancy
from src.vacancy_container import VacancyContainer
from tests.conftest import temp_file


def test_add_vacancy(json_saver, vacancy, temp_file):
    json_saver.add_vacancy(vacancy)

    with open(temp_file.name, 'r', encoding='utf-8') as f:
        data = json.load(f)

    assert vacancy.__dict__ in data


