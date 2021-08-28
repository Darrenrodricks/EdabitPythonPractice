# Write a Python program to convert the distance (in feet) to inches, yards, and miles.

a = int(input("Input distance in feet: "))
x_inches = round(a * 12, 3)
x_yards = round(a / 3.0, 3)
x_miles = round(a / 5280.0, 3)

print("The distance in inches is {} inches.".format(x_inches))
print("The distance in yards is {} yards.".format(x_yards))
print("The distance in miles is {} miles.".format(x_miles))