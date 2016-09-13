# create a function that takes a list and returns a new list that is reversed

my_list = [5, 68, 49, 654, 2, 11]

def reverse_list(a):
    new_list = []
    for i in range(0, len(a)):
        new_list += [a[len(a) - 1 - i]]
    return new_list

print(reverse_list(my_list))
