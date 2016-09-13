# create a function that returns it's input factorial

def fact(a):
    b = 1
    for i in range(1, a+1):
        b *= i
    return b

print(fact(5))
