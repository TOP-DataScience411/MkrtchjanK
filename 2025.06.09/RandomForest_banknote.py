import pandas as pd
from pathlib import Path
from sys import path

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, fbeta_score
from sklearn.model_selection import train_test_split

# Загружаем датасет
data_path = Path(path[0]) / "banknote-auth.csv"
df = pd.read_csv(data_path)

# Целевая переменная и признаки
y = df["class"]
X = df.drop(columns="class")

# Делим данные на тренировочную и тестовую выборки (80%/20%)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1
)

# Обучаем модель случайного леса
clf = RandomForestClassifier(
    n_estimators=25,
    max_depth=5,
    bootstrap=True,
    n_jobs=-1,
    random_state=1
)

clf.fit(X_train, y_train)

# Получаем предсказания
y_pred = clf.predict(X_test)

# Матрица ошибок
cm = confusion_matrix(y_test, y_pred)
tn, fp, fn, tp = cm.ravel()

# Расчёт метрик
accuracy = (tp + tn) / cm.sum()
specificity = tn / (tn + fp) if (tn + fp) != 0 else 0
precision = tp / (tp + fp) if (tp + fp) != 0 else 0
recall = tp / (tp + fn) if (tp + fn) != 0 else 0
f1_score = 2 * precision * recall / (precision + recall) if (precision + recall) != 0 else 0
fbeta_val = fbeta_score(y_test, y_pred, beta=0.5)

print("Оценка модели на тестовой выборке:")
print(f"Accuracy (Точность):         {accuracy:.1%}")
print(f"Specificity (Специфичность): {specificity:.1%}")
print(f"Precision (Прецизионность):  {precision:.1%}")
print(f"Recall (Полнота):            {recall:.1%}")
print(f"F1-мера:                     {f1_score:.1%}")
print(f"F0.5-мера:                   {fbeta_val:.1%}")