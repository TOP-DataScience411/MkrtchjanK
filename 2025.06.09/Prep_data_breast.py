import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from pathlib import Path
from sys import path

# Путь к текущей папке
base_path = Path(path[0])

# Загружаем встроенный датасет из sklearn
breast_data = load_breast_cancer()

# Преобразуем в DataFrame для удобной работы
features = pd.DataFrame(breast_data.data, columns=breast_data.feature_names)
labels = pd.Series(breast_data.target, name="target")

# Быстрая проверка на пропущенные значения (для отчёта)
if features.isnull().values.any():
    print("В данных есть пропущенные значения!")
else:
    print("Пропущенных значений нет.")

# Нормализация: (значение - среднее) / стандартное отклонение
# Используем describe() для единообразия
means = features.describe().loc["mean"]
stds = features.describe().loc["std"]
normalized = (features - means) / stds

# Добавляем целевой столбец
normalized["target"] = labels

# Сохраняем обработанные данные
normalized.to_csv(base_path / "breast_cancer_filter.csv", index=False)

# Построим гистограмму одной переменной — например, mean radius
plt.figure(figsize=(6, 4))
plt.hist(features["mean radius"], bins=25, color="skyblue", edgecolor="black")
plt.title("Распределение: mean radius")
plt.xlabel("Значение")
plt.ylabel("Частота")
plt.grid(True)
plt.tight_layout()
plt.savefig(base_path / "mean_radius_distribution.png", dpi=150)
plt.close()

print("Файл breast_cancer_filter.csv сохранён. Дополнительно сохранена гистограмма.")