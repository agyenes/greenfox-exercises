# Create a function that takes a list as a parameter,
# and returns a new list with every second element from the orignal list
# It should raise an error if the parameter is not a list
# example: [1, 2, 3, 4, 5] should produce [2, 4]

def list_of_every_second_element_of_input(input_list):
    if type(input_list) != list:
        raise ValueError('Parameter not a list')
    new_list = []
    for i in range(1,len(input_list)+1):
        if i % 2 == 0:
            new_list.append(input_list[i-1])
    return new_list

print(list_of_every_second_element_of_input([7, 5, 6, 7, 8, 2]))
print(list_of_every_second_element_of_input([7, 'g', 6, 'banán', 8.67, 2]))
print(list_of_every_second_element_of_input('sd'))
