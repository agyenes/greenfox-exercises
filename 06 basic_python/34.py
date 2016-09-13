numbers = [4, 5, 6, 7, 8, 9, 10]
# write your own sum function


def sum(list):
    a = 0
    for i in list:
        a += i
    return a

print(sum(numbers))
