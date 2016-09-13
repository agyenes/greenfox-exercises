
# Adds a and b, returns as result
def add(a, b):
    if type(a) != int or type(b) != int:
        print("gimme an int!")
        return ""
    return a+b

# Returns the highest value from the three given params
def max_of_three(a, b, c):
    if type(a) != int or type(b) != int or type(c) != int:
        print("gimme an int!")
        return ""
    if a > b and a > c:
        return a
    elif b > c:
        return b
    elif a == b and a > c and a > b:
        return a, b
    else:
        return c

# Returns the median value of a list given as param
def median(pool):
    if type(pool) != list:
        print("gimme a list!")
        return ""
    else:
        if len(pool) % 2 == 0:
            return (pool[int(len(pool)/2)-1] + pool[int(len(pool)/2) + 1])/2
        else:
            return pool[int((len(pool) - 1) / 2)]

# Returns true if the param is a vovel
def is_vovel(char):
    if type(char) != str:
        print("gimme a string!")
        return ""
    else:
        return char in 'aeiouöüóőúéáűí'

# Create a method that translates hungarian into the teve language
def translate(hungarian):
    if type(hungarian) != str:
        print("gimme a string!")
        return ""
    teve = hungarian
    for char in teve:
        if is_vovel(char):
            teve = (char+'v'+char).join(teve.split(char))
    return teve
