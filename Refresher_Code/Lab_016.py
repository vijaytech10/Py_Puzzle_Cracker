"""
numList = [30, 2, -15, 17, 9, 100]
numbers_greater_10 *
"""

# ***** Approach 1: *****
numList = [30, 2, -15, 17, 9, 100]
def value_10_checker(num):
    return num >= 10

output = filter(value_10_checker, numList)
print(list(output))

# ***** Approach 2: *****
numList = [30, 2, -15, 17, 9, 100]
output = filter(lambda num : num >= 10, numList)
print(list(output))
