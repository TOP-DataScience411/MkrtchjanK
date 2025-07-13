import pandas as pd
from pathlib import Path
from sys import path

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import BaggingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
    root_mean_squared_error
)

# Загружаем датасет
base_path = Path(path[0])
dataset = pd.read_csv(base_path / "boston_filter.csv")

# Отделяем целевой столбец (цены домов)
y = dataset["MEDV"]
X = dataset.drop(columns="MEDV")

# Делим данные на тренировочные и тестовые (70%/30%)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1
)

# Создаем ансамбль на основе линейной регрессии
regressor = BaggingRegressor(
    estimator=LinearRegression(),
    n_estimators=17,
    bootstrap=True,
    n_jobs=-1,
    random_state=1
)

# Обучаем модель
regressor.fit(X_train, y_train)

# Получаем предсказания на тестовых данных
predictions = regressor.predict(X_test)

# Вычисляем метрики качества модели
mae_val = mean_absolute_error(y_test, predictions)  # средняя абсолютная ошибка
mse_val = mean_squared_error(y_test, predictions)   # средняя квадратичная ошибка
rmse_val = root_mean_squared_error(y_test, predictions)  # корень из MSE
r2_val = r2_score(y_test, predictions)  # коэффициент детерминации R^2

print("Результаты регрессии на тестовых данных:")
print(f"MAE (средняя абсолютная ошибка):     {mae_val:.4f}")
print(f"MSE (средняя квадратичная ошибка):   {mse_val:.4f}")
print(f"RMSE (корень из MSE):                {rmse_val:.4f}")
print(f"R² (доля объяснённой дисперсии):     {r2_val:.4f}")