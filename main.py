# from re import search
#
#
# def user_interaction():
#     platforms = ["HeadHunter"]
#     search_query = input("Введите поисковый запрос:\n")
#     top_n = int(input("Введите предел количества вакансий ТОП-N:\n"))
#     filter_word = input("Введите ключевые слова для фильтрации:\n")
#     salary_range = input("Введите диапазон зарплат и фалюту в виде: 1000 - 2000 USD:\n")
#
#
# if __name__ == "__main__":
#     user_interaction()
# import json
# import os.path
#
# # Открываем файл с указанием кодировки CP1251
# with open(os.path.join('data', 'vacancies.json'), encoding='utf-8') as f:
#     json_info = json.load(f)
#
# # Сохраняем файл с отступами
# with open(os.path.join('data', 'vacancies_indented.json'), 'w', encoding='utf-8') as f:
#     json.dump(json_info, f, indent=4, ensure_ascii=False)
# from src.vacancy import Vacancy
from tests.conftest import vacancy_1

# TEST FILE READING AND WRITING -- PASSED
# !!!ВАЖНО  test_file.json должен существовать и в нём должно быть '[]'
from src.json_saver import JSONSaver
from src.vacancy import Vacancy
from src.vacancy_container import VacancyContainer

vacancy_1 = Vacancy(
    'Software Developer',
    'https://example.com/job/1',
    5000,
    10000,
    'USD'
)

vacancy_2 = Vacancy(
        'Software Developer',
        'https://example.com/job/2',
        5000,
        10000,
        'USD'
)

json_saver = JSONSaver('test_file.json')
container = VacancyContainer([vacancy_1, vacancy_2])

json_saver.add_vacancy(vacancy_1)
json_saver.add_vacancy(vacancy_2)
