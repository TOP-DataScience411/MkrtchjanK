import pandas as pd
from datetime import datetime
from numpy import array
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Словарь русских месяцев
months_ru_en = {
    'янв': 'Jan', 'фев': 'Feb', 'мар': 'Mar', 'апр': 'Apr',
    'май': 'May', 'июн': 'Jun', 'июл': 'Jul', 'авг': 'Aug',
    'сен': 'Sep', 'окт': 'Oct', 'ноя': 'Nov', 'дек': 'Dec'
}

def parse_russian_dates(file_path):
    data_raw = pd.read_csv(file_path, header=None).iloc[:, 0]
    data_parsed = []
    for entry in data_raw:
        date_str, val = entry.split()
        for ru, en in months_ru_en.items():
            date_str = date_str.replace(ru, en)
        date_parsed = datetime.strptime(date_str, "%d.%b.%y")
        data_parsed.append((date_parsed, float(val.replace(',', '.'))))
    return data_parsed

# Загрузка данных
diesel = parse_russian_dates("dizel_fuel_rus_prices.csv")
urals = parse_russian_dates("urals_oil_rus_export_prices.csv")

# Объединение по году и месяцу
records = []
for d in diesel:
    for u in urals:
        if d[0].year == u[0].year and d[0].month == u[0].month:
            records.append((d[0], d[1], u[1]))
records = array(records)

# Перебор сдвигов
max_offset = len(records) - 2
correlations = []
for offset in range(-max_offset, max_offset + 1):
    if offset > 0:
        x_vals = records[:-offset, 1]
        y_vals = records[offset:, 2]
    elif offset < 0:
        x_vals = records[-offset:, 1]
        y_vals = records[:offset, 2]
    else:
        x_vals = records[:, 1]
        y_vals = records[:, 2]
    if len(x_vals) > 2:
        coef = round(np.corrcoef(x_vals, y_vals)[0, 1], 4)
        print(f"Сдвиг: {offset} месяцев -> корреляция: {coef}")
        correlations.append((coef, offset, x_vals, y_vals))

# Лучшая корреляция и регрессия
top_corr, top_offset, dx, dy = max(correlations, key=lambda x: abs(x[0]))
reg = linregress(dx, dy)
print(f"\nЛучшая корреляция: {top_corr}, при сдвиге {top_offset}")
print(f"Регрессия: y = {reg.intercept:.2f} + {reg.slope:.2f} * x")

# Добавим шум к данным
np.random.seed(42)
dx_jitter = dx + np.random.normal(0, 1.0, size=dx.shape)
dy_jitter = dy + np.random.normal(0, 5.0, size=dy.shape)

# Визуализация
plt.figure(figsize=(10, 6))
plt.scatter(dx_jitter, dy_jitter, s=10, label="Данные с шумом")
plt.plot(dx_jitter, reg.intercept + reg.slope * dx_jitter, linestyle='--', color='green',
         label=f"y = {reg.intercept:.2f} + {reg.slope:.2f} * x")
plt.title(f"Анализ зависимости цен (альтернативный вариант)")
plt.xlabel("Дизель (руб/т)")
plt.ylabel("Urals ($/баррель)")
plt.grid(True)
plt.legend()
plt.savefig("sisters_regression_plot.png", dpi=300)
