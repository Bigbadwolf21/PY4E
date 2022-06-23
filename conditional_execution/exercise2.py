"""
Exercise 2: Rewrite your pay program using try and except so that your
program handles non-numeric input gracefully by printing a message
and exiting the program. The following shows two executions of the
program:
Enter Hours: 20
Enter Rate: nine
Error, please enter numeric input
Enter Hours: forty
Error, please enter numeric input
"""
hour = input("Enter hours worked here: ")
rt = input("Enter your rate here: ")
try:
  hour = float(hour)
  rate = float(rt)
  pay = hour * rate
except:
  print("Error, please enter numeric input")  
