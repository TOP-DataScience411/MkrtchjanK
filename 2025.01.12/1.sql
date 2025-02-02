Запросы к таблице doctors:

1. Вывести средний оклад (salary) всех сотрудников
SELECT ROUND(AVG(salary), 2) AS avg_salary
FROM doctors;

 avg_salary
------------
   59441.30

2. Вывести среднюю премию для всех сотрудников, чей доход выше среднего (взять явное значение из результата предыдущего запроса)

SELECT ROUND(AVG(premium), 2) AS avg_premium 
FROM doctors 
WHERE salary > 59441.3;


Запросы к таблице vacations:
3. Вывести с сортировкой по возрастанию среднее количество дней в отпуске для каждого сотрудника

SELECT AVG(end_date - start_date) AS days, doctor_id
FROM vacations
GROUP BY doctor_id
ORDER BY days ASC;

4. Вывести для каждого сотрудника самый ранний год отпуска и самый поздний год отпуска с сортировкой по возрастанию разности между этими двумя значениями
SELECT MIN(EXTRACT(YEAR FROM start_date)) AS earliest_vacation_year,
MAX(EXTRACT(YEAR FROM end_date)) AS latest_vacation_year, doctor_id
FROM vacations
GROUP BY doctor_id
ORDER BY (end_date - start_date) ASC;

Запросы к таблице donations:

5. Вывести сумму пожертвований за всё время для каждого отделения с сортировкой по возрастанию номеров отделений
SELECT  SUM(amount) as total_donations, dep_id
FROM donations
GROUP BY dep_id
ORDER BY dep_id ASC;

6. Вывести сумму пожертвований за каждый год для каждого спонсора с сортировкой по возрастанию номеров спонсоров и годов
SELECT SUM(amount) as total_year_donations, extract(year from date), sponsor_id
FROM donations
GROUP BY sponsor_id, extract(year from date)
ORDER BY sponsor_id ASC, extract(year from date) ASC;