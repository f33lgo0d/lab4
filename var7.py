import math

total_sum = 0.0

for n in range(1, 51):
    n_to_n = n ** n
    numerator = n_to_n + 1
    denominator = 2 * n_to_n + 1
    fraction = numerator / denominator
    sin_value = math.sin(2 * n**2 + 1)
    term = fraction * sin_value
    total_sum += term

print("Сумма равна:", total_sum)
