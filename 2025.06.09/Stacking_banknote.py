import pandas as pd
from pathlib import Path
from sys import path

from sklearn.model_selection import train_test_split
from sklearn.ensemble import StackingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import LinearSVC
from sklearn.metrics import confusion_matrix, fbeta_score

# Загружаем данные
file_path = Path(path[0]) / "banknote-auth.csv"
df = pd.read_csv(file_path)

# Целевая переменная и признаки
y = df["class"]
X = df.drop(columns="class")

# Делим на тренировочную и тестовую выборки (20% на обучение)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=0.2, random_state=42
)

# Создаем стек из базовых моделей + финальную модель
stack_model = StackingClassifier(
    estimators=[
        ("forest", RandomForestClassifier(n_estimators=10, random_state=42)),
        ("tree", DecisionTreeClassifier(max_depth=6)),
        ("svc", LinearSVC(random_state=42))
    ],
    final_estimator=LogisticRegression(),
    n_jobs=-1
)

# Обучение модели
stack_model.fit(X_train, y_train)

# Предсказание
y_pred = stack_model.predict(X_test)

# Матрица ошибок
cm = confusion_matrix(y_test, y_pred)
tn, fp, fn, tp = cm.ravel()

# Расчёт метрик
accuracy = (tp + tn) / cm.sum()
specificity = tn / (tn + fp) if (tn + fp) != 0 else 0
precision = tp / (tp + fp) if (tp + fp) != 0 else 0
recall = tp / (tp + fn) if (tp + fn) != 0 else 0
f1 = 2 * precision * recall / (precision + recall) if (precision + recall) != 0 else 0
f05 = fbeta_score(y_test, y_pred, beta=0.5)

print("Метрики качества стек-модели:")
print(f"Accuracy (Точность):         {accuracy:.1%}")
print(f"Specificity (Специфичность): {specificity:.1%}")
print(f"Precision (Прецизионность):  {precision:.1%}")
print(f"Recall (Полнота):            {recall:.1%}")
print(f"F1-мера:                     {f1:.1%}")
print(f"F0.5-мера:                   {f05:.1%}")