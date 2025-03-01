import re

months = (
    'января', 'январь',
    'февраля', 'февраль',
    'марта', 'март',
    'апреля', 'апрель',
    'мая', 'май',
    'июня', 'июнь',
    'июля', 'июль',
    'августа', 'август',
    'сентября', 'сентябрь',
    'октября', 'октябрь',
    'ноября', 'ноябрь',
    'декабря', 'декабрь'
)

MONTH_PATTERN = f"(?:{'|'.join(months)})"
YEAR = r"(\d{4})\sг\."  
YEAR_RANGE = r"(\d{4}–\d{4})\sгг\."  

PATTERN = re.compile(
    rf"^({YEAR}|{MONTH_PATTERN}\s{YEAR}|\d{{1,2}}\s{MONTH_PATTERN}\s{YEAR})\s—.*$|^{YEAR}$|^{MONTH_PATTERN}\s{YEAR}$|^({YEAR_RANGE})\s—.*$|^{YEAR_RANGE}$",
    re.MULTILINE,
)

with open(r'C:\Users\user\Desktop\pythonhm\history_dates_ed.txt', encoding="utf-8") as file:
    text = file.read()

result = PATTERN.findall(text)

for res in result:
    for item in res:
        if item:
            print(item) 
            break