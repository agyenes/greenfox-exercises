numbers = [3, 4, 5, 6, 7]
# write a function that filters the odd numbers
# from a list and returns a new list consisting
# only the evens

def filter(list):
    for i in list:
        if i % 2 == 1:
            list.remove(i)
    return list

print(filter(numbers))