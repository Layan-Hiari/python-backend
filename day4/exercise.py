def find_second_largest(nums):
    if len(nums) < 2:
        return None  
    largest = second = float('-inf')
    for num in nums:
        if num > largest:
            second = largest
            largest = num
        elif largest > num > second:
            second = num

    return second if second != float('-inf') else None


def merge_dictionaries(dict1, dict2):
    return dict1 | dict2  

numbers = [12, 45, 2, 41, 31, 10]
second_largest = find_second_largest(numbers)
print("Second Largest Number:", second_largest)

dict_a = {'a': 1, 'b': 2}
dict_b = {'b': 3, 'c': 4}
merged = merge_dictionaries(dict_a, dict_b)
print("Merged Dictionary:", merged)
