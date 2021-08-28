# Write a function that takes two integers (hours, minutes), converts them to seconds, and adds them.
def hours_mins(hours, mins):
    hours *= 3600
    mins *= 60
    print(hours + mins)

hours_mins(1, 3)

hours_mins(2, 0)

hours_mins(0, 0)