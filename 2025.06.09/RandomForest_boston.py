import pandas as pd
from pathlib import Path
from sys import path

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
    root_mean_squared_error
)

csv_path = Path(path[0]) / "boston_filter.csv"
df = pd.read_csv(csv_path)

# Целевая переменная — цена жилья (MEDV)
y = df["MEDV"]
X = df.drop(columns="MEDV")

# Делим выборку: 70% для обучения, 30% для теста
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1
)

# Обучаем модель случайного леса для регрессии
regressor = RandomForestRegressor(
    n_estimators=100,
    max_depth=15,
    bootstrap=True,
    n_jobs=-1,
    random_state=1
)

regressor.fit(X_train, y_train)

# Предсказываем цены на тестовой выборке
y_pred = regressor.predict(X_test)

# Расчёт метрик качества модели
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = root_mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Результаты модели Random Forest:")
print(f"MAE (средняя абсолютная ошибка):     {mae:.4f}")
print(f"MSE (средняя квадратичная ошибка):   {mse:.4f}")
print(f"RMSE (корень из MSE):                {rmse:.4f}")
print(f"R2 (доля объяснённой дисперсии):     {r2:.4f}")