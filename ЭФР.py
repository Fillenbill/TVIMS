import csv
import numpy as np
import matplotlib.pyplot as plt

def empirical_cdf(data):
    """
    Функция для построения эмпирической функции распределения.

    Параметры:
    - data: массив наблюдаемых значений случайной величины.

    Возвращает:
    - x: массив отсортированных значений.
    - y: массив значений эмпирической функции распределения.
    """
    # Отсортировать наблюдаемые значения в порядке возрастания.
    sorted_data = np.sort(data)

    # Создать массив относительных частот.
    n = len(sorted_data)
    y = np.arange(1, n+1) / n

    # Вернуть отсортированные значения и соответствующие значения эмпирической функции распределения.
    return sorted_data, y


if __name__ == "__main__":
    filename = "var_16_lognorm.csv"
    column = read_csv_file(filename)
    column.sort()
    x_ecdf, y_ecdf = empirical_cdf(column)

     # Выводим значения на график
    plt.plot(x_ecdf, y_ecdf)
    plt.show()
