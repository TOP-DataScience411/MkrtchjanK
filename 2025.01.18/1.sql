Запросы к таблицам схемы world:
    
1. Вывести названия стран и названия сопоставленных им столиц
SELECT 
    сountry.Name, 
    city.Name
FROM country 
INNER JOIN city 
    ON country.Capital = city.ID;

2. Сравнить по регионам сумму населения стран и сумму населения городов
SELECT 
    country.Region,
    SUM(country.Population),
    SUM(city.Population)
FROM country 
INNER JOIN city 
    ON country.Code = city.CountryCode
GROUP BY country.Region;


3. Вывести десять языков, на которых разговаривает больше всего людей
SELECT 
    cl.Language,
    SUM(country.Population * cl.Percentage / 100) AS Total_speakers
FROM countrylanguage as cl
JOIN country
    ON cl.CountryCode = country.Code
GROUP BY cl.Language
ORDER BY Total_speakers DESC
LIMIT 10;

Запросы к таблицам схемы hospital:

4. Вывести названия специальностей и суммарное количество дней отпусков, в которых были врачи каждой специальности; отсортировать по возрастанию суммарного количества дней отпуска

SELECT
    sp.name,
    coalesce(sum(end_date - start_date), 0) AS total_vacation_days
FROM specializations as sp
JOIN doctors_specs as ds 
    ON sp.id = ds.spec_id
JOIN vacations as v 
    ON ds.doctor_id = v.doctor_id
GROUP BY sp.name
ORDER BY total_vacation_days ASC;


5. Вывести округлённую до целого сумму средств, которую можно выделить на одну палату этого отделения (в зависимости от количества палат в отделении), от всех пожертвований каждому отделению; отсортировать по убыванию найденной суммы

SELECT
    dep.id,
    dep.name,
    ROUND(SUM(don.amount) / COUNT(DISTINCT wards.id)) AS amount_ward
FROM departments as dep
JOIN wards ON dep.id = wards.dep_id
JOIN donations as don 
    ON dep.id = don.dep_id
GROUP BY dep.id, dep.name
ORDER BY amount_ward DESC;