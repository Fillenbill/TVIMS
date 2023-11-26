import numpy as np
import pandas as pd

def is_valid_number(s):
    try:
        float(s.replace(',', '.'))
        return True
    except ValueError:
        return False

def estimate_lognormal_moments(data):
    # Convert data to numerical values and filter out non-positive values
    data_numeric = [float(d.replace(',', '.')) for d in data if is_valid_number(d)]
    data_numeric = np.array(data_numeric)
    
    # Filter out non-positive values (zeros and negatives)
    positive_data = data_numeric[data_numeric > 0]

    if len(positive_data) == 0:
        raise ValueError("All data points are non-positive. Cannot calculate moments.")

    mean_data = np.mean(positive_data)
    variance_data = np.var(positive_data, ddof=1)  # Using sample variance with ddof=1

    s_moments = np.sqrt(np.log(1 + (variance_data / (mean_data ** 2))))
    loc_moments = np.log(mean_data) - 0.5 * s_moments ** 2

    return loc_moments, s_moments

def estimate_lognormal_mle(data):
    # Convert data to numerical values and filter out non-positive values
    data_numeric = [float(d.replace(',', '.')) for d in data if is_valid_number(d)]
    data_numeric = np.array(data_numeric)
    
    # Filter out non-positive values (zeros and negatives)
    positive_data = data_numeric[data_numeric > 0]

    if len(positive_data) == 0:
        raise ValueError("All data points are non-positive. Cannot calculate MLE.")

    log_data = np.log(positive_data)
    mean_log_data = np.mean(log_data)
    std_log_data = np.std(log_data)

    s_mle = std_log_data
    loc_mle = np.exp(mean_log_data - 0.5 * s_mle ** 2)

    return loc_mle, s_mle

# Read the first 300 numbers from column A in the Excel file
filename = 'var_16_lognorm.csv'
data = pd.read_csv(filename, usecols=[0], nrows=300, sep=';', header=None)
data = data.values.flatten()  # Flatten the 2D array to a 1D array

# Estimate parameters using Method of Moments
try:
    loc_moments, scale_moments = estimate_lognormal_moments(data)
    print('Method of Moments - Estimated loc:', loc_moments)
    print('Method of Moments - Estimated scale:', scale_moments)
except ValueError as e:
    print(f'Method of Moments - {e}')

# Estimate parameters using Maximum Likelihood Estimation
try:
    loc_mle, scale_mle = estimate_lognormal_mle(data)
    print('\nMaximum Likelihood Estimation - Estimated loc:', loc_mle)
    print('Maximum Likelihood Estimation - Estimated scale:', scale_mle)
except ValueError as e:
    print(f'Maximum Likelihood Estimation - {e}')
