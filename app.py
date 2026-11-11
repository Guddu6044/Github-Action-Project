# Take year input from the user
# Leap Year App

year = int(input("Enter a year: "))

# Check leap year conditions
if (year % 400 == 0) and (year % 100 == 0):
  print(f"{year} is a leap year")
elif (year % 4 == 0) and (year % 100 != 0):
  print(f"{year} is a leap year")
else:
  print(f"{year} is not a leap year")

# This code is for know for a Leap year
