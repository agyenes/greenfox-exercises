# 5. We have a number of bunnies and each bunny has two big floppy ears.
# We want to compute the total number of ears across all the bunnies
# recursively (without loops or multiplication).

def power(base, n):
    if n <= 2:
        return base * base
    else:
        return base * power(base, n-1)

print(power(4, 5))
