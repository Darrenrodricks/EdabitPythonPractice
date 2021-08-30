# Python program to count Even and Odd numbers in a List
# Input: list1 = [2, 7, 5, 64, 14]
# Output: Even = 3, odd = 2
a = 0
b = 0
list1 = [2, 7, 5, 64, 14]
for i in range(0, len(list1)):
    if i % 2 == 0:
        a += 1
    else:
        b += 1

print("There are {} Even, and {} Odd".format(a, b))