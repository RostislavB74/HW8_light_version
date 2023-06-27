from datetime import datetime, timedelta
from collections import defaultdict


users = [
    {'name': 'Rostyslav Bysko', 'birthday': datetime(1974, 4, 25)},
    {'name': 'Sergey Korchuk', 'birthday': datetime(1976, 7, 25)},
    {'name': 'Alexandr Korchuk', 'birthday': datetime(1984, 10, 20)},
    {'name': 'Viktor Bakharev', 'birthday': datetime(1962, 6, 23)},
    {'name': 'Svetlana Vratskaya', 'birthday': datetime(1974, 7, 4)},
    {'name': 'Fedor Bulko', 'birthday': datetime(1980, 7, 3)},
    {'name': 'Srgey Gudilin', 'birthday': datetime(1972, 7, 3)},
    {'name': 'Vladimir Metelev', 'birthday': datetime(1982, 12, 31)},
    {'name': 'Dmitry Kryvsha', 'birthday': datetime(1988, 7, 1)},
    {'name': 'Leonid Chayka', 'birthday': '6-7-1949'},
]


def current_data():
    # current_data = datetime(2023, 6, 25)
    # current_date = datetime(2023, 12, 30)  # not tested change year
    # current_date = datetime(2023, 2, 23) # test 29 february not leap
    # current_date = datetime(2024, 2, 23) # test 29 february leap
    # print(current_date)  #
    current_data = datetime.now()

    return (current_data)


def get_birthdays_per_week(list_of_emp: list) -> None:
    result = defaultdict(list)
    current_date = current_data().date()
    current_year = current_data().year
    for users in list_of_emp:
        bd = users["birthday"]

        if isinstance(bd, datetime):
            bd = bd.date()
        else:
            bd = datetime.strptime(bd, "%d-%m-%Y").date()
        if bd.month == 2 and bd.day == 29 and not (current_year % 4 == 0 and
                                                   (current_year % 100 != 0 or
                                                    current_year % 400 == 0)):
            bd = bd.replace(day=1, month=3, year=current_year)

        bd = bd.replace(year=current_year)
        start, end = get_period()
       # print(start, end)
       # print(bd)
        if start <= bd <= end:

            if bd.weekday() in (5, 6):
                bd = current_date + timedelta(days=7-(current_date.weekday()))
                result[bd].append(users['name'])
            else:
                result[bd].append(users['name'])

    return result


def get_period():
    current_date = current_data()

    start_period = current_date + timedelta(days=5-(current_date.weekday()))

    return start_period.date(), (start_period + timedelta(6)).date()


if __name__ == "__main__":
    for key, value in get_birthdays_per_week(users).items():
        # print(key)
        # print(value)
        result = sorted(get_birthdays_per_week(users).items())
        # print(result)
    for i in result:
        list1 = ', '.join(i[1])
        print(f'{i[0].strftime("%A")}: {list1}')
        # print(f'{result.key}:{result.value})')
        # print(f'{key.strftime("%A")}:', value)
        # print(sorted(get_birthdays_per_week(users).items()))
