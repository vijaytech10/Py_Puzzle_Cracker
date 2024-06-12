"""
*** Sample Programs ***
1. Write a Python program to find the largest number in a list.
2. Write a Python program to find the smallest humber in a list.
3. Write a Python program to sum all numbers in a list.
4. Write a Python program to multiply all numbers in a list.
5. Write a Python program to count (and results) of the number of strings in a list where the string length is 2 or more
and the first and last character are the same ?
"""

def find_largest_number(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

def find_smallest_number(numbers):
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num

def sum_all_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def multiply_all_numbers(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def find_strings_with_same_first_and_last_character(strings):
    matching_strings = []  # Initialize an empty list to store matching strings
    count = 0
    for string in strings:
        if len(string) >= 2 and string[0] == string[-1]:
            matching_strings.append(string)  # Append matching strings to the list
            count += 1
    print(count)
    return matching_strings

# Sample usage:
numbers = [10, 20, 30, 40, 50]
strings = ["radar", "hello", "level", "world", "noon"]

print("Largest number:", find_largest_number(numbers))
print("Smallest number:", find_smallest_number(numbers))
print("Sum of all numbers:", sum_all_numbers(numbers))
print("Product of all numbers:", multiply_all_numbers(numbers))
print("Count of strings with same first and last character:", find_strings_with_same_first_and_last_character(strings))

