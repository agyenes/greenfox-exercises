
# create a function that takes a number and divides ten with it and prints the result
# it should print "fail" if it is divided by 0

def divider(num):
    try:
        result = 10/num
        return result
    except ZeroDivisionError:
        print("fail")

print(divider(7))
print(divider(0))
