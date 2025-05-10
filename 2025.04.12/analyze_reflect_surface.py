
from pathlib import Path as P
from sys import path as pth
from pandas import read_csv as rc
import seaborn as s; import matplotlib.pyplot as m
from sklearn.metrics import confusion_matrix as cm, fbeta_score as fs
from sklearn.model_selection import train_test_split as tts
from sklearn.linear_model import LogisticRegression as LR

D = P(pth[0])
F = rc(D / 'reflective_surface_data.csv')
X, Y = F.iloc[:, :-1], F['label']
Xn = (X - X.describe().loc['mean']) / X.describe().loc['std']

m.figure(figsize=(10, 6))
s.boxplot(data=X)
m.savefig(D / 'box_outlier_view.png')

X1, X2, Y1, Y2 = tts(Xn, Y, test_size=0.3, random_state=101, stratify=Y)
mdl = LR(class_weight='balanced').fit(X1, Y1)
Yp = mdl.predict(X2)
(TN, FP), (FN, TP) = cm(Y2, Yp)

a = (TN + TP) / (TN + FP + FN + TP)
s = TN / (TN + FP)
p = TP / (TP + FP)
r = TP / (TP + FN)
f1 = 2 * p * r / (p + r)
fb = fs(Y2, Yp, beta=0.1)

print(f'{a = :.1%}', f'{s = :.1%}', f'{p = :.1%}', f'{r = :.1%}', f'{f1 = :.1%}', f'{fb = :.1%}', sep='\n')
