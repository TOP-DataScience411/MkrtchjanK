from datetime import date, timedelta
from itertools import cycle

# Функция создает расписание дат, начиная с заданной даты, включая определенные дни недели, исключая даты, попадающие в период отпусков.

def schedule(start_date: date, first_weekday: int, *weekdays: int, total_days: int, date_format: str = '%d/%m/%Y'):
    vacations = globals().get('vacations', [])
    dates = []
    current_date = start_date
    weekdays = [first_weekday] + list(weekdays)   

    while len(dates) < total_days:
        if current_date.weekday() + 1 in weekdays:  
            if not any(start <= current_date < start + duration for start, duration in vacations):  
                dates.append(current_date.strftime(date_format))
        current_date += timedelta(days=1)  

    return dates
    
#>>> vacations = [(date(2023, 5, 1), timedelta(weeks=1)),(date(2023, 7, 17), timedelta(weeks=1)),]
#>>> py321 = schedule(date(2023, 4, 1), 6, 7, total_days=70)
#>>> len(py321)  
#70
#>>> py321[28:32]
#['15/07/2023', '16/07/2023', '29/07/2023', '30/07/2023']
