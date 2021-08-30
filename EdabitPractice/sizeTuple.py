import sys
# sample Tuples
Tuple1 = ("A", 1, "B", 2, "C", 3)
Tuple2 = ("Geek1", "Raju", "Geek2", "Nikhil", "Geek3", "Deepanshu")
Tuple3 = ((1, "Lion"), ( 2, "Tiger"), (3, "Fox"), (4, "Wolf"))

# print the sizes of sample Tuples
print(str(sys.getsizeof(Tuple1)) + "bytes")
print(str(sys.getsizeof(Tuple2)) + "bytes")
print(str(sys.getsizeof(Tuple3)) + "bytes")