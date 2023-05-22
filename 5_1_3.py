import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erf

def plot_theoretical_cdf(data, loc, scale):
    # Ограничиваем данные по оси X до максимального значения в выборке
    data_max = np.max(data)
    x = np.linspace(0, data_max, 100)

    # Вычисляем теоретическую функцию распределения (CDF)
    cdf = 0.5 + 0.5 * erf((np.log(x) - loc) / (np.sqrt(2) * scale))

    # Построение графика
    plt.plot(x, cdf, label='Theoretical CDF')
    plt.title('Theoretical CDF')
    plt.xlabel('Value')
    plt.ylabel('Cumulative Probability')
    plt.legend()
    plt.show()

# Считываем данные из файла
data = []
with open('var_16_lognorm.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        data.append(float(row[0]))

# Ограничиваем данные по оси X до 200
data = [x for x in data if x <= 200]

# Задаем параметры распределения
loc = 0 # Значение loc должно быть положительным
scale = 1


# Построение теоретической функции распределения
plot_theoretical_cdf(data, loc, scale)
