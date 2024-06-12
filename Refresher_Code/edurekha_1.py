def shout (text):
    return text.upper() + "!"

def whisper (text):
    return text.lower() +".."

def greet(func, name):
    message = func(name)
    print(message)

# Output :
greet(shout, "Hello")
greet(whisper, "Hello")