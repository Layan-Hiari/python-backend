def alternating_signs(numbers):
    sign = 1
    for num in numbers:
        yield sign * abs(num)
        sign *= -1

input_numbers = [1, -2, 3, -4, 5, -6]

for num in alternating_signs(input_numbers):
    print(num)
