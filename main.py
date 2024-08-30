from fileinput import filename

from src.hh_api_client import HHAPIClient
from src.json_saver import JSONSaver
from src.vacancy import Vacancy
from src.vacancy_container import VacancyContainer


def user_interaction() -> None:
    # PRIMARY INPUT
    print('Greetings!')
    search_query = input('Enter your query:\n')
    top_n = input('Enter the number of vacancies to display:\n')

    # Creating client
    hh_client = HHAPIClient()

    # Casting Vacancies
    hh_vacancies = hh_client.load_vacancies(search_query)
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

    # Creating container
    vac_container = VacancyContainer(vacancies_list)

    # Using some features
    # FILTERING
    keyword = input('Enter keyword for filtering or skip (leave it blank):\n')
    keyword = keyword.strip()
    if not keyword:
        print('You decided to skip')
        filtered = vac_container
    else:
        filtered = vac_container.filtered_by(keyword)

    # RANGING / SORTING
    ranging = input("Enter 'Y' to sort vacancies or skip by entering anything else:\n")
    if not 'y' in ranging:
        ranged = filtered
    else:
        ranged = filtered.ranged()

    # Creating JSON connector
    file_name = input('Enter name of a new file:\n')
    json_saver = JSONSaver(file_name)
    json_saver.container_extend(ranged)

    top_vacancies = json_saver.get_vacancies().get_top_n(top_n)
    print(top_vacancies)


if __name__ == '__main__':
    user_interaction()
