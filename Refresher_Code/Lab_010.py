# Palindrome Checker

def palindrome_checker(word):
    word = word.lower()
    reverse_word = word[::-1]
    if word == reverse_word:
        print("The word {} is a perfect palindrome".format(word))
    else:
        print(f"The word {word} is not a palindrome")
    print ('exit')

word = input("Enter the word for Palindrome test : ")
palindrome_checker(word)
