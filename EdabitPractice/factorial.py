# Create a function that takes an integer and returns the factorial of that integer.
# That is, the integer multiplied by all positive lower integers.

def factorial(x):
    if x == 0:
        return 1
    return x * factorial(x-1)

print(factorial(5))