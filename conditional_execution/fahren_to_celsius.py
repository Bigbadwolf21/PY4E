# Convert Fahrenheit to Celsius
input_fahren = input("Enter your temperature in Fahrenheit here: ")
try:
  fahren = float(input_fahren)
  celsius = (fahren - 32) * 5/9
  print(celsius)
except:
  print("Please enter a number")  
