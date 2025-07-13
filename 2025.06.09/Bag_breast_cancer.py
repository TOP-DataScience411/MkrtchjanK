import pandas as pd
from pathlib import Path
from sys import path

from sklearn.model_selection import train_test_split
from sklearn.ensemble import BaggingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, fbeta_score

# Загружаем данные из файла
current_path = Path(path[0])
df = pd.read_csv(current_path / "breast_cancer_filter.csv")

# Целевая переменная и признаки
y = df["target"]
X = df.drop(columns="target")

# Разделяем данные на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Создаём ансамбль логистических регрессий
classifier = BaggingClassifier(
    estimator=LogisticRegression(),
    n_estimators=7,
    bootstrap=True,
    n_jobs=-1,
    random_state=42
)

# Обучаем модель
classifier.fit(X_train, y_train)

# Получаем предсказания
y_pred = classifier.predict(X_test)

# Считаем матрицу ошибок
matrix = confusion_matrix(y_test, y_pred)
tn, fp, fn, tp = matrix.ravel()

# Метрики классификации
accuracy = (tp + tn) / matrix.sum()
specificity = tn / (tn + fp) if (tn + fp) != 0 else 0
precision = tp / (tp + fp) if (tp + fp) != 0 else 0
recall = tp / (tp + fn) if (tp + fn) != 0 else 0
f1 = 2 * precision * recall / (precision + recall) if (precision + recall) != 0 else 0
f05 = fbeta_score(y_test, y_pred, beta=0.5)

print("Оценка модели на тестовой выборке:")
print(f"Точность (Accuracy):       {accuracy:.1%}")
print(f"Специфичность (Specificity): {specificity:.1%}")
print(f"Точность (Precision):      {precision:.1%}")
print(f"Полнота (Recall):          {recall:.1%}")
print(f"F1-мера:                   {f1:.1%}")
print(f"F0.5-мера:                 {f05:.1%}")