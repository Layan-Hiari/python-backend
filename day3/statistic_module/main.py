import statistic

numbers = [25, 36, 49, 64, 81, 100, 121]


mean = statistic.calculate_mean(numbers)
median = statistic.calculate_median(numbers)
stdev = statistic.calculate_stdev(numbers)


print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Standard Deviation: {stdev}")


number = 64
sqrt_value = statistic.calculate_square_root(number)
log_value = statistic.calculate_logarithm(number)


print(f"Square root of {number}: {sqrt_value}")
print(f"Logarithm of {number}: {log_value}")
