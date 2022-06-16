"""
Exercise 3: Write a program to prompt the user for hours and rate per
hour to compute gross pay.
Enter Hours:35
Enter Rate: 2.75
Pay: 96.25
"""

input_hours = input("Enter the numbers of hours worked here: ")
hours = float(input_hours)
input_rate = input("Enter your charge rate here: ")
rate = float(input_rate)
# Compute pay
pay = hours * rate
print("Your pay is $", pay)
