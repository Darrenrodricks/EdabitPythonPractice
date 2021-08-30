# Python program to create a list of tuples from given list having number and its cube in each tuple
def square_tuple():
    a = list()
    for i in range(1, 20):
        a.append(i **3)
    print(tuple(a))

square_tuple()
    