# """
# Problem - 1
# i/p: "chaandrasekaran"
# o/p: "c1h1a2n1d1r1a1s1e2k1"
# """
# def count_characters(input_string):
#     """Counts the occurrences of each character in a string and returns a dictionary."""
#     char_counts = {}
#     for char in input_string:
#         if char in char_counts:
#             char_counts[char] += 1
#         else:
#             char_counts[char] = 1
#     return char_counts
#
#
# # Prompt the user for input
# input_string = input("Enter a string: ")
#
# # Check if input_string is empty
# if not input_string:
#     print("Input string is empty.")
# else:
#     # Call the function to count characters
#     char_counts = count_characters(input_string)
#
#     # Create the output string with character-count combinations
#     output_string = ""
#     for char, count in char_counts.items():
#         output_string += f"{char}{count}"
#     print("Output:", output_string)
#
# print(output_string)  # Output : c1h1a2n1d1r1a1s1e2k1

"""
Problem - 2
i/p:  chaandrasekaran kumar vijay
o/p: vijay kumar chaandrasekaran
list = [chaandrasekaran, kumar, vijay]
"""

def name_reverser_a(str_list):
    # Create a reversed copy using slicing
    rev_list = str_list[::-1]
    print("rev_list is : ", rev_list)
    new_list = "-".join(rev_list)
    print ("new_list is : ", new_list)
    return new_list


def name_reverser_b(str_list):
    # Create a reversed copy using reversed()
    rev_list = reversed(str_list)
    new_list = " ".join(rev_list)
    return new_list


input_name = "chaandrasekaran kumar vijay"
ip_chars = input_name.split(" ")
print(ip_chars)

# Call both functions - Solutions
reversed_name_a = name_reverser_a(ip_chars)
#reversed_name_b = name_reverser_b(ip_chars)

print(reversed_name_a)  # Output: vijay kumar chaandrasekaran
#print(reversed_name_b)  # Output: vijay kumar chaandrasekaran (same output)