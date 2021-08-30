# Python program to print even numbers in a list
a = [2, 7, 5, 64, 14]
a = list(filter(lambda x: x % 2 == 0, a))
a.sort()
print(a)