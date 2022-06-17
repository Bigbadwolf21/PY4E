"""
Exercise 5: Write a program which prompts the user for a Celsius temperature,
convert the temperature to Fahrenheit, and print out the converted temperature.
 """
cels_temp = input("Enter your temperature in Celsius here: ")
celsius = float(cels_temp)
fahrenheit = (9/5) * celsius + 32
print(celsius, "degree celsius is ", fahrenheit, "degree fahrenheit")
