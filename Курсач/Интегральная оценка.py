from scipy.stats import norm

n = 300
x_bar = 18.5229
sigma = 108.3813
confidence_level = 0.95

alpha = 1 - confidence_level
alpha_div_2 = alpha / 2

z = norm.ppf(1 - alpha_div_2)

C_j = sigma * z / (n ** 0.5)

lower_bound = x_bar - C_j
upper_bound = x_bar + C_j

print("Значение C_j:", C_j)
print("Интервал оценки для параметра theta: ({:.4f}, {:.4f})".format(lower_bound, upper_bound))
