# Create a program that determines whether a given year is a leap year.
# Leap year Checker
# A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.

# Take input for the year
year = int(input("Enter the year: "))

# Check if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")