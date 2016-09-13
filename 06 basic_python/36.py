numbers = [3, 4, 5, 6, 7]
# write a function that reverses a list

def reverse(list):
    reverse = []
    for i in range(len(list)-1, -1, -1):
        reverse += [list[i]]
    return reverse

print(reverse(numbers))
