names = ['Zakarias', 'Hans', 'Otto', 'Ole']
# create a function that returns the shortest string
# from a list


def shortest(input):
    min = input[0]
    for i in input:
        if len(i) < len(min):
            min = i
    return min

print(shortest(names))
