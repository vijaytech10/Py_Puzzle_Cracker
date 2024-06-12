# Create a lambda function to triple power(cube) (2**3) a number.
def cube_generator(num):
    result = num**3
    return result

num = int(input("Enter number to be cubed : "))
print (cube_generator(num))

# *********** Lambda Approach ***********
cube_generator = lambda num: num**3

num = int(input("Enter number to be cubed : "))
print(cube_generator(num))
