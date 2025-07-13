import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from sys import path

file_path = Path(path[0]) / "boston.csv"

raw_data = pd.read_csv(file_path, comment="#")

# Проверка: есть ли пропущенные значения?
missing = raw_data.isnull().sum().sum()
if missing > 0:
    print(f"Внимание: в данных есть {missing} пропущенных значений.")
else:
    print("Пропущенные значения не найдены.")

# Удаляем строки с максимальным значением MEDV (считается выбросом)
raw_data = raw_data[raw_data["MEDV"] != raw_data["MEDV"].max()]

# Отдельно сохраняем целевую переменную
target = raw_data["MEDV"]

# Удаляем признаки, которые мешают обучению модели (на основе корреляции)
columns_to_drop = ["DIS", "CHAS", "NOX", "TAX", "MEDV"]
filtered_data = raw_data.drop(columns=columns_to_drop)

# Нормализация признаков
normalized_data = (filtered_data - filtered_data.mean()) / filtered_data.std()

# Добавляем целевую переменную обратно
normalized_data["MEDV"] = target

#Небольшая визуализация — распределение цен
plt.figure(figsize=(8, 4))
plt.hist(target, bins=25, edgecolor='black')
plt.title("Распределение цен на жильё (MEDV)")
plt.xlabel("Цена")
plt.ylabel("Частота")
plt.grid(True)
plt.tight_layout()
plt.savefig(Path(path[0]) / "price_distribution.png", dpi=150)
plt.close()

# Сохраняем подготовленные данные
normalized_data.to_csv(Path(path[0]) / "boston_filter.csv", index=False)

print("Обработка завершена. Файл boston_filter.csv успешно сохранён.")