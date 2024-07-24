import random
from datetime import datetime, timedelta
from pathlib import Path


def get_random_sex() -> str:
    sex = ('Male', 'Female')
    return random.choice(sex)


def get_random_male_name() -> str:
    male_names = []
    male_names_path = Path.cwd() / 'names_randomizer' / 'male names.txt'
    with male_names_path.open(mode='r', encoding='utf-8') as file:
        for row in file:
            male_names.append(row.rstrip('\n'))
    return str(random.choice(male_names)).capitalize()


def get_random_female_name() -> str:
    female_names = []
    female_names_path = Path.cwd() / 'names_randomizer' / 'female names.txt'
    with female_names_path.open(mode='r', encoding='utf-8') as file:
        for row in file:
            female_names.append(row.rstrip('\n'))
    return str(random.choice(female_names)).capitalize()


def get_random_surname() -> str:
    surnames = []
    surnames_path = Path.cwd() / 'names_randomizer' / 'surnames.txt'
    with surnames_path.open(mode='r', encoding='utf-8') as file:
        for row in file:
            surnames.append(row.rstrip('\n'))
    return str(random.choice(surnames)).capitalize()


def get_random_birthdate(start: str = '1960-01-01', end: str = '2005-01-01', date_format: str = '%Y-%m-%d') -> str:
    start_date = datetime.strptime(start, date_format)
    end_date = datetime.strptime(end, date_format)
    delta = end_date - start_date
    days_diff = delta.days
    random_date = start_date + timedelta(days=days_diff) * random.random()
    return random_date.strftime(date_format)


def get_random_full_name(sex: str) -> str:
    if sex == 'Male':
        name = get_random_male_name()
        surname = get_random_surname()
        return surname + ' ' + name
    elif sex == 'Female':
        name = get_random_female_name()
        surname = get_random_surname()
        return surname + ' ' + name


def get_random_f_surname() -> str:
    surnames = []
    surnames_path = Path.cwd() / 'names_randomizer' / 'surnames.txt'
    with surnames_path.open(mode='r', encoding='utf-8') as file:
        for row in file:
            if row.lower().startswith('f'):
                surnames.append(row.rstrip('\n').lower())
    return str(random.choice(surnames)).capitalize()


def get_F_full_name() -> str:
    name = get_random_male_name()
    surname = get_random_f_surname()
    return surname + ' ' + name

