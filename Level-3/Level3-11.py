'''
11. Make a temperature/measurement converter. Write a script that can convert
Fahrenheit to Celcius and back, or inches to centimeters and back, etc in 3 different
ways
'''
temp = input("Input the  temperature you like to convert: ")
degree = int(temp[:-1])
i_convention = temp[-1]

if i_convention.upper() == "C":
  result = int(round((9 * degree) / 5 + 32))
  o_convention = "Fahrenheit"
elif i_convention.upper() == "F":
  result = int(round((degree - 32) * 5 / 9))
  o_convention = "Celsius"
else:
  print("Input proper convention.")
  quit()
print("The temperature in", o_convention, "is", result, "degrees.")
