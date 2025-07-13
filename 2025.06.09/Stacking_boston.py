import pandas as pd
from pathlib import Path
from sys import path

from sklearn.model_selection import train_test_split
from sklearn.ensemble import StackingRegressor, RandomForestRegressor
from sklearn.linear_model import LinearRegression, RidgeCV
from sklearn.svm import LinearSVR

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
    root_mean_squared_error
)

# Загружаем подготовленные данные
file_path = Path(path[0]) / "boston_filter.csv"
df = pd.read_csv(file_path)

# Целевая переменная и признаки
y = df["MEDV"]
X = df.drop(columns="MEDV")

# Делим данные на обучающую и тестовую выборки (30% для обучения)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=0.3, random_state=1
)

# Создаем стек из моделей регрессии
reg_stack = StackingRegressor(
    estimators=[
        ("ridge", RidgeCV()),
        ("linreg", LinearRegression()),
        ("svr", LinearSVR(random_state=1))
    ],
    final_estimator=RandomForestRegressor(n_estimators=30, random_state=1),
    n_jobs=-1
)

# Обучаем стек-регрессию
reg_stack.fit(X_train, y_train)

# Предсказываем значения на тестовой выборке
y_pred = reg_stack.predict(X_test)

# Вычисляем метрики
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = root_mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Результаты стек-регрессии:")
print(f"MAE (средняя абсолютная ошибка):     {mae:.4f}")
print(f"MSE (средняя квадратичная ошибка):   {mse:.4f}")
print(f"RMSE (корень из MSE):                {rmse:.4f}")
print(f"R² (доля объяснённой дисперсии):     {r2:.4f}")