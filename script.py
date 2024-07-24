from database_folder.database import Database
from database_folder.user_data import UserData
from names_randomizer import randomizer
import logging
from datetime import datetime
import time


logger = logging.getLogger(__name__)
logging.basicConfig(level='INFO',
                    format='#%(levelname)-8s [%(asctime)s] %(filename)s: %(lineno)d - %(name)s - %(message)s')


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time} seconds")
        return result
    return wrapper


def task_1() -> None:
    db = Database()
    db.create_table(full_name='VARCHAR(255)', birth_date='DATE', sex='VARCHAR(10)', age='INT')


def task_2(full_name: str, birthdate: str, sex: str) -> None:
    if not _check_full_name(full_name):
        print('Incorrect data entered')
        return None
    elif not _validate_date(birthdate):
        print('Incorrect data entered')
        return None
    elif not _check_sex(sex):
        print('Incorrect data entered')
        return None
    data = UserData(full_name=full_name, birth_date=birthdate, sex=sex)
    db = Database()
    values = [[data.full_name, data.birth_date, data.sex, data.get_age()]]
    db.insert_rows('full_name', 'birth_date', 'sex', 'age', values=values)

# def task_2() -> None:
#     request_data = True
#     values = []
#     while request_data:
#         full_name = input('Enter full name. Format: Surname Name Patronymic. Here: ')
#         if not _check_full_name(full_name):
#             print('Incorrect data entered')
#             continue
#         birth_date = input('Enter birthdate. Format: YYYY-MM-DD. Here: ')
#         if not _validate_date(birth_date):
#             print('Incorrect data entered')
#             continue
#         sex = input('Enter sex. Format: Male or Female. Here:  ')
#         if not _check_sex(sex):
#             print('Incorrect data entered')
#             continue
#         data = UserData(full_name=full_name, birth_date=birth_date, sex=sex)
#         values.append([data.full_name, data.birth_date, data.sex, data.get_age()])
#         another_data = str(input("Would you like to insert more data? Please, answer 'yes' or 'no', other answers "
#                                  "will cause the program to insert the previous data and shut down. Enter: "))
#         if another_data.lower() not in ['yes', 'y', '1', 'да']:
#             request_data = False
#     db = Database()
#     db.insert_rows('full_name', 'birth_date', 'sex', 'age', values=values)


def _check_full_name(full_name: str) -> bool:
    if full_name.isdigit():
        return False
    return True


def _validate_date(date: str) -> bool:
    try:
        datetime.strptime(date, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def _check_sex(sex: str) -> bool:
    if sex.lower() not in ['male', 'female']:
        return False
    return True


def task_3() -> None:
    db = Database()
    db.select_distinct_and_sort_rows('full_name', 'CAST(birth_date AS CHAR) as birth_date', 'sex', 'age',
                                     order_by='full_name')


def task_4() -> None:
    # Заполнение автоматически 1_000_000 строк справочника сотрудников выполняется 16 минут(((
    # 100% есть более оптимизированный вариант исполнения
    # Чтобы долго не ждать, снизил кол-во записей до 10_000. Чтобы вставить 1_000_000 записей, нужно увеличить кол-во
    # итераций в первом цикле до 1000
    db = Database()
    for i in range(10):
        obj_list = []
        for j in range(1000):
            j = UserData(full_name='', birth_date=randomizer.get_random_birthdate(), sex=randomizer.get_random_sex())
            j.full_name = randomizer.get_random_full_name(j.sex)
            obj_list.append(j)
        db.insert_rows('full_name', 'birth_date', 'sex', 'age',
                       values=db.convert_obj_list_into_values_list(obj_list))
    # Заполнение автоматически 100 строк в которых пол мужской и фамилия начинается с "F".
    obj_list = []
    for i in range(100):
        j = UserData(full_name='', birth_date=randomizer.get_random_birthdate(), sex='Male')
        j.full_name = randomizer.get_F_full_name()
        obj_list.append(j)
    db.insert_rows('full_name', 'birth_date', 'sex', 'age',
                   values=db.convert_obj_list_into_values_list(obj_list))


@timer
def task_5() -> None:
    db = Database()
    db.task5()

def task_6() -> None:
    print('Из-за нехватки времени я не сделал 6 задание (по личным обстоятельствам я мало уделил времени этому '
          'тестовому заданию)\n'
          'Я знаю, что оптимизировать запрос можно с помощью индексирования, но я этого пока не умею :(')