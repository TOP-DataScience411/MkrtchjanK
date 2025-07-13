import numpy as np
from scipy import stats

# Исходные данные
N = np.array([311, 354, 438, 368, 450, 384, 506, 397, 565, 417])
R = np.array([506, 559, 512, 552, 532, 553, 535, 576, 546, 574, 548, 609, 551, 632])

# Уровень значимости
alpha = 0.05

# 1. Проверка крайних членов на принадлежность генеральной совокупности (критерий Диксона)
def dixon_test(data, left=True):
    n = len(data)
    data_sorted = np.sort(data)
    if left:
        # Проверка минимального значения
        r = (data_sorted[1] - data_sorted[0]) / (data_sorted[-1] - data_sorted[0])
    else:
        # Проверка максимального значения
        r = (data_sorted[-1] - data_sorted[-2]) / (data_sorted[-1] - data_sorted[0])
    # Критические значения для n=10 и n=14 (из таблиц Диксона)
    critical_values = {
        10: {0.05: 0.477},
        14: {0.05: 0.347}
    }
    critical = critical_values[n][alpha]
    return r < critical

# Проверка для N (n=10)
min_N_outlier = dixon_test(N, left=True)
max_N_outlier = dixon_test(N, left=False)

# Проверка для R (n=14)
min_R_outlier = dixon_test(R, left=True)
max_R_outlier = dixon_test(R, left=False)

print("Проверка крайних значений на выбросы:")
print(f"Минимальное значение N - выброс: {min_N_outlier}")
print(f"Максимальное значение N - выброс: {max_N_outlier}")
print(f"Минимальное значение R - выброс: {min_R_outlier}")
print(f"Максимальное значение R - выброс: {max_R_outlier}")

# 2. Проверка равенства дисперсий (критерий Левене, т.к. нет предположения о нормальности)
levene_test = stats.levene(N, R)
print("\nПроверка равенства дисперсий (Левене):")
print(f"p-value: {levene_test.pvalue:.4f}")
if levene_test.pvalue > alpha:
    print("Гипотеза о равенстве дисперсий НЕ отвергается.")
else:
    print("Гипотеза о равенстве дисперсий отвергается.")

# 3. Проверка равенства средних (t-критерий Стьюдента)
# Если дисперсии равны, используем параметр equal_var=True
t_test = stats.ttest_ind(N, R, equal_var=(levene_test.pvalue > alpha))
print("\nПроверка равенства средних (t-критерий):")
print(f"p-value: {t_test.pvalue:.4f}")
if t_test.pvalue > alpha:
    print("Гипотеза о равенстве средних НЕ отвергается.")
else:
    print("Гипотеза о равенстве средних отвергается.")

# 4. Проверка нормальности распределения (Шапиро-Уилк)
shapiro_N = stats.shapiro(N)
shapiro_R = stats.shapiro(R)
print("\nПроверка нормальности распределения (Шапиро-Уилк):")
print(f"p-value для N: {shapiro_N.pvalue:.4f}")
if shapiro_N.pvalue > alpha:
    print("Гипотеза о нормальности для N НЕ отвергается.")
else:
    print("Гипотеза о нормальности для N отвергается.")
print(f"p-value для R: {shapiro_R.pvalue:.4f}")
if shapiro_R.pvalue > alpha:
    print("Гипотеза о нормальности для R НЕ отвергается.")
else:
    print("Гипотеза о нормальности для R отвергается.")