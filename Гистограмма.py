import csv
import numpy as np
import matplotlib.pyplot as plt

# Считываем данные из файла
data = []
with open('var_16_lognorm.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        data.append(float(row[0]) + 2.118733)

# Ограничиваем данные по оси X до 180
data = [x for x in data if x <= 180]

# Функция расчета интегральной кривой
def calculate_cumulative(data):
    x, y = np.unique(sorted(data)), np.arange(1, len(np.unique(sorted(data))) + 1)
    return x, y/y[-1]

# Функция построения графика
def plot_cumulative(x, y, label):
    plt.plot(x, y, label=label)

# Разбиваем данные на 50 интервалов и строим гистограмму
plt.hist(data, bins=50, density=True)

# Строим интегральные кривые
np.random.seed(42)
sample_sizes = [200]
for sample_size in sample_sizes:
    sample = np.random.choice(data, sample_size)
    x, y = calculate_cumulative(sample)
    plot_cumulative(x, y, label=f'n={sample_size}')

# Оформляем график
plt.title('Lognormal distribution')
plt.xlabel('Value')
plt.ylabel('Cumulative probability')
plt.legend()
plt.show()
