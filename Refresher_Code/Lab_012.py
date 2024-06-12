"""
*** Sample Programs ***
1. Count Vowels & constants in a string

"""
# Answer 1
string = str(input("Enter the string for segregation into Vowels & constants : "))
string = list(string.lower())
vowels = ['a', 'e', 'i', 'o', 'u']
op_vow = []
op_con = []
count_vow = 0
count_con = 0
for x in string:
    if x in vowels:
        count_vow += 1
        op_vow.append(x)
    else:
        count_con += 1
        op_con.append(x)
op_vow = ''.join(op_vow)
op_con = ''.join(op_con)

print(f"The new word formed using vowels in given word is : {op_vow}, with count as : {count_vow}")
print(f"The new word formed using constants  in given word is : {op_con}, with count as : {count_con}")
