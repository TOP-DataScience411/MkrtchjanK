import pandas as pd
import numpy as np
from pathlib import Path

# Пути к данным
base_path = Path(".")
file_science = base_path / "science_investetions.csv"
file_cancer = base_path / "early_malignancy.csv"

# Загрузка и обработка данных
def load_and_clean(path, skip):
    data = pd.read_csv(path, skiprows=skip, header=None)
    data = data.iloc[:, 0].str.split(expand=True)
    data.columns = ['Year', 'Value']
    data['Year'] = data['Year'].astype(int)
    data['Value'] = data['Value'].astype(float)
    return data

science = load_and_clean(file_science, 20)
cancer = load_and_clean(file_cancer, 19)

# Объединение по годам
joined = pd.merge(science, cancer, on="Year", how="inner", suffixes=('_science', '_cancer')).sort_values("Year")

# Нормализация значений
def normalize(series):
    return (series - series.min()) / (series.max() - series.min())

joined['science_norm'] = normalize(joined['Value_science'])
joined['cancer_norm'] = normalize(joined['Value_cancer'])

# Проверка корреляций со сдвигом
def test_lags(df, col1, col2, max_lag=5):
    results = []
    for lag in range(-max_lag, max_lag + 1):
        temp = df.copy()
        if lag > 0:
            temp[col1] = temp[col1].shift(lag)
        elif lag < 0:
            temp[col2] = temp[col2].shift(-lag)
        temp = temp.dropna()
        if len(temp) > 2:
            r = np.corrcoef(temp[col1], temp[col2])[0, 1]
            print(f"Сдвиг: {lag} лет")
            print(f"{col1}: {temp[col1].tolist()}")
            print(f"{col2}: {temp[col2].tolist()}")
            print(f"Корреляция: {round(r, 4)}\n")
            results.append((lag, r))
    return results

# Запуск анализа
correlations = test_lags(joined, 'science_norm', 'cancer_norm', max_lag=5)

# Лучшая корреляция
if correlations:
    top_lag, top_corr = max(correlations, key=lambda x: abs(x[1]))
    print(f"Макс. корреляция: {round(top_corr, 4)} при сдвиге {top_lag} лет")
