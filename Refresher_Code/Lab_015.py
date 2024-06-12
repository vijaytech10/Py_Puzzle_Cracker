"""
Create function with parameter that can perform x^y
Try both Normal &
"""
def power_multiplier(x,y):
    result = x**y
    print("the exponent output is {}".format(result))

x = int(input("Enter the number to be made exponent (or) Multiplied :"))
y = int(input("Enter the power value to be multiplied :"))
power_multiplier(x,y)

# *********** Lambda Approach ***********
power_multiplier = lambda x, y : x**y

x = int(input("Enter the number to be made exponent (or) Multiplied: "))
y = int(input("Enter the power value to be multiplied: "))
print("The exponent output is", power_multiplier(x, y))
