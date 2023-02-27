# (ii). a Python program to find if a given string starts with a given character using Lambda. 

str = input('Enter a string: ')
startVar = input('Enter a character to check if the string starts with it: ')
start = lambda x: x.startswith(startVar)
if start(str) == True:
    print(f"{str} starts with {startVar}")
else:
    print(f"{str} does not start with {startVar}")

