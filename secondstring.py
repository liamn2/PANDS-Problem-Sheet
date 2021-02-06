# secondstring.py
# Code that takes input sentence and outputs every second letter in reverse order.
# Author: Liam Nutley

# First we create our input section for the user. 
word=(input("Enter Sentence: "))
# we define the users input as our string.
str = word
# String length (number of characters) defined.
stringlength=len(str)
# String slice reverses users input string.
slicedString=str[stringlength::-1]
# String slice takes out every second letter in the reversed input and we print the result.
print(slicedString[::2])