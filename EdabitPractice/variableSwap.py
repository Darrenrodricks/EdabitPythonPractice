# Swapping two variables refers to mutually exchanging the values of the variables. Generally, this is done with the data in memory.
#
# The simplest method to swap two variables is to use a third temporary variable :

a = 30
b = 20
print("\nBefore swap a = {} and b = {}".format(a, b))
a, b = b, a
print("\nAfter swaping a = {} and b = {}".format(a, b))
print()