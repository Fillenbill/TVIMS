import csv
import numpy as np
import matplotlib.pyplot as plt

def empirical_cdf(data):
    
       return 1
    
def read_csv_file(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        column = []
        for row in reader:
            column.append(float(row[0]))
        return column

def sample_sum(sample):
    return sum(sample)

def sample_mean(sample):
    return sum(sample) / len(sample)

def sample_median(sample):
    n = len(sample)
    if n % 2 == 0:
        sample.sort()
        return (sample[n//2] + sample[n//2+1]) / 2
    else:
        return sample[n//2]

def sample_mode(sample):
    freq_dict = {}
    for x in sample:
        freq_dict[x] = freq_dict.get(x, 0) + 1
    max_freq = max(freq_dict.values())
    if max_freq == 1:
        return 0
    else:
        most_common_num = [k for k, v in freq_dict.items() if v == max_freq]
        return most_common_num[0]

def sample_range(sample):
    return max(sample) - min(sample)

def sample_variance(sample, biased=True):
    n = len(sample)
    mean = sample_mean(sample)
    variance = sum((x - mean)**2 for x in sample) / (n if biased else n-1)
    return variance

def sample_moment(sample, k):
    n = len(sample)
    mean = sample_mean(sample)
    moment = sum(x**k for x in sample) / n
    return moment

def sample_central_moment(sample, k):
    n = len(sample)
    mean = sample_mean(sample)
    cent_moment = sum((x - mean)**k for x in sample) / n
    return cent_moment


if __name__ == "__main__":
    filename = "var_16_lognorm.csv"
    column = read_csv_file(filename)
    column.sort()
    print("Column:", column)
    print("\nSample Sum:", sample_sum(column))
    print("Sample Mean:", sample_mean(column))
    print("Sample Median:", sample_median(column))
    print("Sample Mode:", sample_mode(column))
    print("Sample Range:", sample_range(column))
    print("Biased Sample Variance:", sample_variance(column, biased=True))
    print("Unbiased Sample Variance:", sample_variance(column, biased=False))
    k = 3
    print(f"Sample {k}-th Moment:", sample_moment(column, k))
    print(f"Sample {k}-th Central Moment:", sample_central_moment(column, k))
   

     # Выводим значения на график
     # plt.plot(x_ecdf, y_ecdf)
    plt.show()
