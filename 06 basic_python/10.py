# Create a function that prints a triangle like this:
#       *
#      ***
#     *****
#    *******
#   *********
#  ***********
#
# It should take a number as parameter that describes how many lines the triangle has

def print_xmastree(lines):
    i = 0
    while i <= lines:
        print((lines - i) * ' ' + (2 * i - 1 ) * '*')
        i += 1

print_xmastree(10)
