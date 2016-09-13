
# 2. write a recursive function
# that takes one parameter: n
# and adds numbers from 1 to n


def recursive_function(n):
    if n <= 1: #base case
        return n
    elif n == 2:
        return n + 1
    else:
        return n + recursive_function(n-1)

print(recursive_function(7))
