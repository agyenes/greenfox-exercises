# 3. Given a non-negative int n,
# return the sum of its digits recursively (no loops).
# Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6),
# while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).

import math

def sum_of_digits(n):
    if n < 10:
        return n
    elif n < 100:
        return n // 10 + n % 10
    else:
        return n % 10 + sum_of_digits(n // 10)

print(sum_of_digits(789785))
