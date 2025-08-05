numbers = [10, 45, 32, 67, 89, 21, 89]

unique_sorted = sorted(set(numbers), reverse=True)

if len(unique_sorted) >= 2:
    second_largest = unique_sorted[1]
else:
    second_largest = None

print("Second Largest Number:", second_largest)

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

merged_dict = dict1 | dict2

print("Merged Dictionary:", merged_dict)
