from mypy.checkpattern import self_match_type_names

from src.vacancy_base import VacancyBase

class Vacancy(VacancyBase):
    """ Represents a vacancy """
    __slots__ = ()

    def __init__(self,
                 name: str,
                 url: str,
                 salary_from: float,
                 salary_to: float,
                 # salary_currency: str,
                 ):
        self.name = name
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to

    # MAGIC METHODS
    def __eq__(self, other):
        if not isinstance(other, Vacancy):
            raise TypeError('Incorrect type for comparison')
        else:
            return self.salary_from == other.salary_from

    def __lt__(self, other):
        if not isinstance(other, Vacancy):
            raise TypeError('Incorrect type for comparison')
        else:
            return self.salary_from < other.salary_from

    def __le__(self, other):
        if not isinstance(other, Vacancy):
            raise TypeError('Incorrect type for comparison')
        else:
            return self.salary_from <= other.salary_from

    def __gt__(self, other):
        if not isinstance(other, Vacancy):
            raise TypeError('Incorrect type for comparison')
        else:
            return self.salary_from > other.salary_from

    def __ge__(self, other):
        if not isinstance(other, Vacancy):
            raise TypeError('Incorrect type for comparison')
        else:
            return self.salary_from >= other.salary_from

    def __str__(self):
        pass

    def __repr__(self):
        pass

    @classmethod
    def cast_to_object_list(cls, vacancies: list[str,...]) -> list[object, ...]:
        """
        Return list of Vacancy objects from list of JSON vacancy info
        :param vacancies: data in JSONFormat
        :return: list of Vacancy objects
        :param vacancies:
        :return:
        """
        result = []
        for vacancy in vacancies:
            pass
        return result

