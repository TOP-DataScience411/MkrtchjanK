import pandas as pd
from pathlib import Path
from sys import path

from sklearn.model_selection import train_test_split
from sklearn.ensemble import (
    StackingClassifier, RandomForestClassifier
)
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.metrics import confusion_matrix, fbeta_score

csv_path = Path(path[0]) / "breast_cancer_filter.csv"
df = pd.read_csv(csv_path)

# Разделяем признаки и целевую переменную
y = df["target"]
X = df.drop(columns="target")

# Делим выборку: 15% — обучение, остальное — тест
X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=0.15, random_state=42
)

# Определяем стек моделей
stacking_clf = StackingClassifier(
    estimators=[
        ("forest", RandomForestClassifier(n_estimators=10, random_state=42)),
        ("tree", DecisionTreeClassifier(max_depth=6)),
        ("svc", LinearSVC(random_state=42))
    ],
    final_estimator=LogisticRegression(),
    n_jobs=-1
)

# Обучаем стек
stacking_clf.fit(X_train, y_train)

# Предсказываем
y_pred = stacking_clf.predict(X_test)

# Матрица ошибок
cm = confusion_matrix(y_test, y_pred)
tn, fp, fn, tp = cm.ravel()

# Метрики качества
accuracy = (tp + tn) / cm.sum()
specificity = tn / (tn + fp) if (tn + fp) != 0 else 0
precision = tp / (tp + fp) if (tp + fp) != 0 else 0
recall = tp / (tp + fn) if (tp + fn) != 0 else 0
f1 = 2 * precision * recall / (precision + recall) if (precision + recall) != 0 else 0
f05 = fbeta_score(y_test, y_pred, beta=0.5)

print("Оценка стек-модели:")
print(f"Accuracy (точность):         {accuracy:.1%}")
print(f"Specificity (специфичность): {specificity:.1%}")
print(f"Precision (прецизионность):  {precision:.1%}")
print(f"Recall (полнота):            {recall:.1%}")
print(f"F1-мера:                     {f1:.1%}")
print(f"F0.5-мера:                   {f05:.1%}")