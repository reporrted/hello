# This is a Python script.
print('Hello World')  # Welcome to the beginning.

print('What is your name?')  # ask for their name
myName = input()  # take input
print('Nice to meet you, ' + myName)  # nice to meet you.
print('The length of your name is:' + str(len(myName)))  # change len to str to concatenate with the previous str.

print('What is your age?')  # ask for their age
myAge = input()  # take input
print('You will be ' + str(int(myAge) + 1) + ' in a year.')  # change myAge to an int so you can add 1, then back to a
# string to print.
