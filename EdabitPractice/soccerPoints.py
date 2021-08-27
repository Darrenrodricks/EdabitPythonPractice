# Create a function that takes the number of wins, draws and losses and calculates the number of points a football team has obtained so far.
def football_points(num1, num2, num3):
    print("You gave scored {} points".format((num1 * 3) + (num2) + (num3 - num3)))

football_points(3, 4, 2)

football_points(5, 0, 2)

football_points(0, 0, 1) 