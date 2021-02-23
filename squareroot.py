# squareroot.py 
# Program that takes a positive floating-point number as input and outputs an approximation of its square root.
# Author: Liam Nutley

import math # Here, We import the math function.

def newton(x): # Define Newton method for square roots. 
   tolerance = 0.000001
   estimate = 1.0
   while True: #<tt>sqrt</tt>
        estimate = (estimate + x / estimate) / 2
        difference = abs(x - estimate ** 2)
        if difference <= tolerance:
            break
   return estimate # Returns our estimate from the above process. 

def main():
   while True: # <tt>sqrt</tt>
       x = input("Enter a positive floating number: ") # User input number here. 
       if x == '':
           break
       x = float(x)
       print("Square root estimate is", newton(x)) # Prints result. 
main()