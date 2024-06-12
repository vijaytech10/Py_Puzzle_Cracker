# Use the ternary operator to find the maximum of three numbers entered by the user.
# Version 1 :
# Take input from the user for three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Compare the numbers using if statements
if num1 >= num2 and num1 >= num3:
    max_num = num1
elif num2 >= num1 and num2 >= num3:
    max_num = num2
else:
    max_num = num3

# Print the maximum number
print("The maximum number is:", max_num)

# Version 2:
# Take input from the user for three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Use ternary operator to find the maximum of three numbers
max_num = num1 if (num1 > num2 and num1 > num3) else (num2 if num2 > num3 else num3)

# Print the maximum number
print("The maximum number is:", max_num)
