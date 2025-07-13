import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import BaggingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, fbeta_score
from pathlib import Path
from sys import path

file_path = Path(path[0]) / "banknote-auth.csv"
data_frame = pd.read_csv(file_path)

# Выделяем признаки и целевую переменную
features = data_frame.drop("class", axis=1)
labels = data_frame["class"]

# Делим выборку на обучающую и тестовую (80/20)
X_train, X_test, y_train, y_test = train_test_split(
    features, labels, test_size=0.2, random_state=1
)

# Создаём ансамбль на основе логистической регрессии
bagging_model = BaggingClassifier(
    estimator=LogisticRegression(),  # базовая модель
    n_estimators=10,                 # количество моделей в ансамбле
    bootstrap=True,                  # использовать бутстрэп
    n_jobs=-1                        # использовать все ядра процессора
)

# Обучаем модель
bagging_model.fit(X_train, y_train)

# Получаем предсказания
predictions = bagging_model.predict(X_test)

# Строим матрицу ошибок
cmatrix = confusion_matrix(y_test, predictions)
tn, fp, fn, tp = cmatrix.ravel()  # распаковываем значения

# Считаем метрики
accuracy = (tp + tn) / (tn + fp + fn + tp)
specificity = tn / (tn + fp) if (tn + fp) != 0 else 0
precision = tp / (tp + fp) if (tp + fp) != 0 else 0
recall = tp / (tp + fn) if (tp + fn) != 0 else 0
f1 = 2 * precision * recall / (precision + recall) if (precision + recall) != 0 else 0
f05 = fbeta_score(y_test, predictions, beta=0.5)

print("Оценка модели на тестовой выборке:")
print(f"Точность (Accuracy):       {accuracy:.2%}")
print(f"Специфичность (Specificity): {specificity:.2%}")
print(f"Точность (Precision):      {precision:.2%}")
print(f"Полнота (Recall):          {recall:.2%}")
print(f"F1-мера:                   {f1:.2%}")
print(f"F0.5-мера:                 {f05:.2%}")