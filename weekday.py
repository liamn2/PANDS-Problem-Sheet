# weekday.py
# Author: Liam Nutley
# Program which determones whether input date is a weekday or the weeekend

# Here, we import our pandas module.
import pandas as pd 
  
# We define our funtion for checking the input date. 
def check_weekday(date): 
      
    # Here, we are computing the parameter date with len function. 
    res=len(pd.bdate_range(date,date)) 
      
    if res == 0 : 
        print("It is the weekend, yay!") 
    else: 
        print("Yes, unfortunately today is a weekday")  
  
# Here is where the user enters their date.
date = (input("Enter the date: "))
check_weekday(date) 
  