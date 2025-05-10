
from pandas import DataFrame
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from numpy import fliplr

raw = load_breast_cancer()
df = DataFrame(raw.data, columns=raw.feature_names)
targets = raw.target

df_scaled = (df - df.mean()) / df.std()

group_0 = df_scaled[targets == 0].mean()
group_1 = df_scaled[targets == 1].mean()
delta = abs(group_0 - group_1)

importance = delta.sort_values(ascending=False)
selected = importance.index

print("Classifier performance by feature blocks:\n")

for block in range(0, 30, 6):
    cols = selected[block:block+6]
    X = df_scaled[cols]
    y = targets

    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

    model = LogisticRegression()
    model.fit(x_train, y_train)
    preds = model.predict(x_test)

    mat = confusion_matrix(1 - y_test, 1 - preds)
    incorrect_ratio = round(sum(fliplr(mat).diagonal()) / sum(mat.sum()), 2)

    print(f"Features {block+1} to {block+6}:")
    print(f"Incorrect prediction rate: {incorrect_ratio}")
    print(mat, end="\n\n")
