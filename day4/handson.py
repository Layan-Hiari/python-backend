numbers = [12, 5, 8, 19, 3, 25, 7, 10]

sorted_numbers = sorted(numbers)

even_numbers = [num for num in numbers if num % 2 == 0]

squared_numbers = [num ** 2 for num in numbers]

numbers_tuple = tuple(numbers)

incremented_tuple = tuple(num + 1 for num in numbers_tuple)

print("Original List:", numbers)
print("Sorted List:", sorted_numbers)
print("Even Numbers:", even_numbers)
print("Squared Numbers:", squared_numbers)
print("Original Tuple:", numbers_tuple)
print("Incremented Tuple:", incremented_tuple)
