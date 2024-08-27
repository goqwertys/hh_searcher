import pytest

from src.vacancy import Vacancy
from src.vacancy_container import VacancyContainer


# VACANCY TEST
@pytest.fixture
def vacancy_1():
    return  Vacancy(
        'Software Developer',
        'https://example.com/job/1',
        5000,
        10000,
        'USD'
    )


@pytest.fixture
def vacancy_2():
    return Vacancy(
        'Software Developer',
        'https://example.com/job/2',
        5000,
        10000,
        'USD'
    )


@pytest.fixture
def vacancy_3():
    return Vacancy(
        'Software Developer',
        'https://example.com/job/3',
        6000,
        10000,
        'USD'
    )


@pytest.fixture
def vacancy_4():
    return Vacancy(
        'Software Developer',
        'https://example.com/job/4',
        7000,
        11000,
        'USD'
    )

@pytest.fixture
def vacancy_5():
    return Vacancy(
        'Web Designer',
        'https://example.com/job/5',
        5000,
        11000,
        'EUR'
    )

# VACANCY CONTAINER
@pytest.fixture
def vacancy_list():
    return [
        Vacancy("Developer", "http://example.com/1", 50000, 70000, "USD"),
        Vacancy("Designer", "http://example.com/2", 40000, 60000, "USD"),
        Vacancy("Manager", "http://example.com/3", 60000, 80000, "USD")
    ]

@pytest.fixture
def vacancy_container(vacancy_list):
    return VacancyContainer(vacancy_list)
