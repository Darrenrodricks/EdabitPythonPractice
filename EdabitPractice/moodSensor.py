# Create a function that takes in a current mood and return a sentence in the following format:
# "Today, I am feeling {mood}". However, if no argument is passed, return "Today, I am feeling neutral".

def mood(str="neutral"):
    print("Today I am feeling {}".format(str))

mood()
mood("happy")
mood("sad")