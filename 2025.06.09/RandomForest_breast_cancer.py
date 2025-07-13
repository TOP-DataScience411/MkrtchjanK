import pandas as pd
from pathlib import Path
from sys import path

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, fbeta_score

# Путь к подготовленному файлу
data_path = Path(path[0]) / "breast_cancer_filter.csv"
df = pd.read_csv(data_path)

# Разделение признаков и целевой переменной
y = df["target"]
X = df.drop(columns="target")

# Делим данные на обучающую и тестовую выборки (80/20)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1
)

# Обучаем модель случайного леса с ограниченной глубиной
clf = RandomForestClassifier(
    n_estimators=6,
    max_depth=4,
    bootstrap=True,
    n_jobs=-1,
    random_state=1
)

clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

# Получаем матрицу ошибок
cm = confusion_matrix(y_test, y_pred)
tn, fp, fn, tp = cm.ravel()

# Вычисляем метрики
accuracy = (tp + tn) / cm.sum()
specificity = tn / (tn + fp) if (tn + fp) != 0 else 0
precision = tp / (tp + fp) if (tp + fp) != 0 else 0
recall = tp / (tp + fn) if (tp + fn) != 0 else 0
f1 = 2 * precision * recall / (precision + recall) if (precision + recall) != 0 else 0
f05 = fbeta_score(y_test, y_pred, beta=0.5)

print("Оценка модели Random Forest на тестовой выборке:")
print(f"Accuracy (Точность):         {accuracy:.1%}")
print(f"Specificity (Специфичность): {specificity:.1%}")
print(f"Precision (Прецизионность):  {precision:.1%}")
print(f"Recall (Полнота):            {recall:.1%}")
print(f"F1-мера:                     {f1:.1%}")
print(f"F0.5-мера:                   {f05:.1%}")