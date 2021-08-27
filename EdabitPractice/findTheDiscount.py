# Create a function that takes two arguments: the original price and the discount
# percentage as integers and returns the final price after the discount.
# dis(1500, 50) ➞ 750
#
# dis(89, 20) ➞ 71.2
#
# dis(100, 75) ➞ 25

def dis(p, d):
    d *= 0.01
    x = d * p
    p -= x
    print(p)

dis(1500, 50)

dis(89, 20)

dis(100, 75)
