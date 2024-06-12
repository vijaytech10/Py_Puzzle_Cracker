# HomeWork 001 - Task 2
"""
Take a input from a user and print the table
(i.e) n = 2 & print - 2 x 1 = 2..... 2 x 10 = 20
"""

#-- Source Code (Version 1) --
def multiplier_table(value, times):
    output = ""
    with open("output_Lab_001_HW_Task02.txt", "w") as file:
        for x in range(1, times+1):
            result = (value * x)
            output_line = f"{value} * {x} = {result}\n"
            print (output_line)
            output+=output_line
            file.write(output_line)
    return output


value = int(input("Which multiplication Table needs to be generated : "))
times = int(input("Enter the number of times <or> the maximum multiplier factor : "))
print(multiplier_table(value, times))


#-- Source Code (Version 2) --

num = int(input("Enter the Table Required : "))
times = int(input("Enter the No. of times Gen Required : "))
for x in range(1, times+1):
    print ("{}x{}={}".format(num,x,(num*x)))
print ("Table generation Completed")



# HomeWork 001 - Task 2
"""
List the all the functions avaiable for the String Data Type.
e.g len()
"""

# Answer
"""
Listing out some of the common string functions in Python:

1. `len(str)`: Returns the length of the string.
2. `str.lower()`: Converts all characters in the string to lowercase.
3. `str.upper()`: Converts all characters in the string to uppercase.
4. `str.capitalize()`: Converts the first character to uppercase and the rest to lowercase.
5. `str.title()`: Converts the first character of each word to uppercase.
6. `str.startswith(prefix)`: Returns `True` if the string starts with the specified prefix.
7. `str.endswith(suffix)`: Returns `True` if the string ends with the specified suffix.
8. `str.strip()`: Removes leading and trailing whitespaces from the string.
9. `str.split()`: Splits the string into a list of substrings based on whitespace by default.
17. `str.islower()`: Returns `True` if all alphabetic characters in the string are lowercase.
18. `str.isupper()`: Returns `True` if all alphabetic characters in the string are uppercase.
19. `str.isnumeric()`: Returns `True` if all characters in the string are numeric.
20. `str.splitlines()`: Splits the string at line breaks and returns a list of lines.

"""