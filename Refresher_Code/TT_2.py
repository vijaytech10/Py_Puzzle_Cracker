list = ['india', 'is', 'my', 'country'] # Dupe Chars across items > i, n, y
str = ''.join(list)
print(str) # Op - indiaismycountry

def find_duplicate_chars(input_str):
    seen = set()
    duplicates = set()
    for char in input_str:
        if char in seen:
            duplicates.add(char)
        seen.add(char)
    return duplicates

result = find_duplicate_chars(str)
print(result)
 # Final Actual Output - {'i', 'n', 'y'}
 # Exepected outpur is
 # String op wih seperator : i, n, y
 # String op wihout seperator : i n y