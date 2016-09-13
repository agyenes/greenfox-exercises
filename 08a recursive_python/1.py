
# 1. write a recursive function
# that takes one parameter: n
# and counts down from n

def recursive_function(n):
    if n <= 1: #base case
        return str(n) + "\n"
    else:
        return str(n) + "\n" + recursive_function(n-1)

print(recursive_function(15))
