import random
import datetime
from pathlib import Path
from typing import Dict, Literal, Optional

names: Dict[str, Dict[str, list]] = {
    'мужской': {'имя': [], 'отчество': [], 'фамилия': []},
    'женский': {'имя': [], 'отчество': [], 'фамилия': []}
}

def load_data() -> None:
    # Функция читает данные из файлов в каталоге data/names и заполняет глобальный словарь names.
    path = Path(r'C:\Users\user\MkrtchjanK\2024.12.14\data\names')
    
    # Загрузка имен и отчеств
    with open(path / 'женские_имена.txt', encoding='utf-8') as f:
        names['женский']['имя'] = [line.strip() for line in f.readlines()]

    with open(path / 'мужские_имена_отчества.txt', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) >= 2:
                names['мужской']['имя'].append(parts[0])
                names['мужской']['отчество'].append(parts[1].strip('(,)'))
                if len(parts) == 3:
                    names['женский']['отчество'].append(parts[2].strip('()'))

    # Загрузка фамилий
    with open(path / 'фамилии.txt', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split(',')
            if len(parts) == 2:
                names['женский']['фамилия'].append(parts[1].strip())
                names['мужской']['фамилия'].append(parts[0].strip())
            elif len(parts) == 1:
                names['мужской']['фамилия'].append(parts[0].strip())
                names['женский']['фамилия'].append(parts[0].strip())
def generate_person() -> Dict[str, Optional[str]]:
    # Функция генерирует анкету человека со случайными данными.
    gender = random.choice(['мужской', 'женский'])
    first_name = random.choice(names[gender]['имя'])
    patronymic = random.choice(names[gender]['отчество'])
    last_name = random.choice(names[gender]['фамилия'])
    
    birth_date = generate_random_date()
    mobile_number = generate_mobile_number()
    
    return {
        'имя': first_name,
        'отчество': patronymic,
        'фамилия': last_name,
        'пол': gender,
        'дата рождения': birth_date,
        'мобильный': mobile_number
    }

def generate_random_date() -> datetime.date:
    # Функция генерирует случайную дату рождения в диапазоне 1923-2023 годов.
    year = random.randint(1923, 2023)
    month = random.randint(1, 12)
    
    # Определяем количество дней в месяце с учетом високосного года
    if month in [1, 3, 5, 7, 8, 10, 12]:
        day = random.randint(1, 31)
    elif month in [4, 6, 9, 11]:
        day = random.randint(1, 30)
    else:  
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            day = random.randint(1, 29)  # Високосный год
        else:
            day = random.randint(1, 28)  # Обычный год
            
    return datetime.date(year, month, day)

def generate_mobile_number() -> str:
    # Функция генерирует случайный мобильный номер в формате +79xxxxxxxxx.
    return '+79' + ''.join(random.choices('0123456789', k=9))


#>>> from pprint import pprint
#>>> load_data()
#>>> pprint(generate_person(), sort_dicts=False)

#{'имя': 'Антон',
#'отчество': 'Степанович',
#'фамилия': 'Кармадонов',
#'пол': 'мужской',
#'дата рождения': datetime.date(1938, 11, 1),
#'мобильный': '+79347189100'}

#{'имя': 'Искра',
#'отчество': 'Поликарповна',
#'фамилия': 'Спутник',
#'пол': 'женский',
#'дата рождения': datetime.date(2016, 11, 6),
#'мобильный': '+79710857811'}