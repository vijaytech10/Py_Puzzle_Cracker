# Fibonacci Series:
a,b = 0,1
n = int(input("Enter Series length : "))
for i in range (n):
    print (f"{a}" + ",", end="\t")
    a, b = b, a+b



