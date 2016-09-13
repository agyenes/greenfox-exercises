# 5. We have a number of bunnies and each bunny has two big floppy ears.
# We want to compute the total number of ears across all the bunnies
# recursively (without loops or multiplication).

def bunny_ear_calculator(n):
    if n <= 2:
        return n * 2
    else:
        return 2 + bunny_ear_calculator(n-1)

print(bunny_ear_calculator(3))
