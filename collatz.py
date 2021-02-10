# collatz.py
# Author: Liam Nutley
# Program that asks the user to input any positive integer and outputs the successive values of the following calculation: At each step, we calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. Have the program end if the current value is one.


def collatz(number):

# Here we set up our code to print and return for even numbers.
    if number % 2 == 0:
        print(number // 2)
        return number // 2

# And here, we identify odd numbers and then we multiply them by 3 and add 1, then print the result.
    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result

# Here, we allow for the users input. 
n = input("Enter a Number: ")
while n != 1:
    n = collatz(int(n))