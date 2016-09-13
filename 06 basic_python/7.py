
# create a function that takes a list and returns a new list with all the elements doubled

my_list = [5, 68, 49, 654, 2, 11]

def doubled_list(a):
    new_list = []
    for i in range(0, len(a)):
        new_list += [a[i]*2]
    return new_list

print(doubled_list(my_list))
