"""
Exercise 1: Rewrite your pay computation to give the employee 1.5
times the hourly rate for hours worked above 40 hours.
Enter Hours: 45
Enter Rate: 10
Pay: 475.0
"""
input_hours = input("Enter the number of hours worked here: ")
hours = float(input_hours)
input_rate = input("Enter your rate here: ")
rate = float(input_rate)
if hours <= 40:
  print("Your Pay is ", hours * rate)
elif hours > 40:
  print("Your Pay is ", 40 * rate + (hours - 40) * 1.5 * rate)
