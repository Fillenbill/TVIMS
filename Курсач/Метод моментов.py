import csv
import matplotlib.pyplot as plt

def read_csv_file(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        column = []
        for row in reader:
            column.append(float(row[0]))
        return column

def calculate_sample_mean(data):
    n = len(data)
    if n == 0:
        return None
    return sum(data) / n

def calculate_sample_variance(data):
    n = len(data)
    if n == 0:
        return None
    mean = calculate_sample_mean(data)
    return sum((x - mean) ** 2 for x in data) / n

if __name__ == "__main__":
    filename = "var_16_lognorm.csv"
    column = read_csv_file(filename)
    column.sort()
    
    # Вычисляем первый и второй моменты (выборочное среднее и выборочная дисперсия)
    sample_mean = calculate_sample_mean(column)  # Первый момент (выборочное среднее)
    sample_variance = calculate_sample_variance(column)  # Второй момент (выборочная дисперсия)
    
    print("Выборочное среднее (первый момент):", sample_mean)
    print("Выборочная дисперсия (второй момент):", sample_variance)
    
    # Выводим значения на график
    plt.plot(column, label='Выборка')
    plt.xlabel('Номер наблюдения')
    plt.ylabel('Значение')
    plt.legend()
    plt.show()