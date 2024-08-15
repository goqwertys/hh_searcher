from re import search


def user_interaction():
    platforms = ["HeadHunter"]
    search_query = input("Введите поисковый запрос:\n")
    top_n = int(input("Введите предел количества вакансий ТОП-N:\n"))
    filter_word = input("Введите ключевые слова для фильтрации:\n")
    salary_range = input("Введите диапазон зарплат и фалюту в виде: 1000 - 2000 USD:\n")


if __name__ == "__main__":
    user_interaction()
