str = 'abc' # print unique chars - e,s

def unique_char_identifier(string):
    unique = []
    for char in string:
        if string.count(char) == 1 and char not in unique:
            unique.append(char)
    return unique

print(unique_char_identifier(str))