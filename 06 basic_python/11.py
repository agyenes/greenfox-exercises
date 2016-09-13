
# Create a function that prints a diamond like this:
#       *
#      ***
#     *****
#    *******
#   *********
#  ***********
#   *********
#    *******
#     *****
#      ***
#       *
#
# It should take a number as parameter that describes how many lines the diamond has

def print_diamond(lines):
    if lines % 2 == 0:
        i = 0
        a = round(lines/2)
        print(a)
        for i in range(0, a + 1):
            print((a - i) * ' ' + (2 * i - 1 ) * '*')
            i += 1
        for i in range(a + 1, lines + 1):
            print((i - a - 1) * ' ' + ((lines - i) * 2 + 1) * '*')
            i += 1
    else:
        i = 0
        a = round(lines/2) + 1
        print(a)
        for i in range(0, a + 1):
            print((a - i) * ' ' + (2 * i - 1 ) * '*')
            i += 1
        for i in range(a + 1, lines + 1):
            print((i - a) * ' ' + ((lines - i) * 2 + 1) * '*')
            i += 1

print_diamond(10)
print_diamond(9)
