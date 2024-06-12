"""
Problem - 1
i/p: "chaandrasekaran"
o/p: "c1-h1-a2-n1-d1-r1-a1-s1-e2-k1..."
"""

def string_counter(string):
    dict = {}
    for char in string:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict

def output_generator(dict):
    output_string = ""
    for keys, values in dict.items():
        output_string = output_string + f"{keys}{values}-"
    output_string = output_string[:-1]
    return output_string

string = ("cchhhannnndd")
print("ip string is : ", string_counter(string))
dicton = string_counter(string)
expected_op = output_generator(dicton)
print("expected op is : ", expected_op)
