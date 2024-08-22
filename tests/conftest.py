import pytest

from src.vacancy import Vacancy
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
