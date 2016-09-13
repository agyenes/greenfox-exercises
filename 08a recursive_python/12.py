# 12. write a recursive function that can add numbers in
# [1, 2, [3, 4], 1, [1, [2, 4]]]

def add_numbers(number):
    list = []
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return add_numbers(number - 1) + add_numbers(number - 2)

print(add_numbers(7))
