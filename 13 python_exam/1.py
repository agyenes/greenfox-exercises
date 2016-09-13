# Create a function that takes a list as a parameter,
# and returns a new list with all it's element value doubled.
# It should raise an error if the parameter is not a list


def doubler(raw_list):
  if type(raw_list) != list:
    raise ValueError('Excepted a list')
  doubled_list = []
  for value in raw_list:
    doubled_list.append(value * 2)
  return doubled_list

print(doubler([7, 5, 6, 7, 8, 2]))
print(doubler('sd'))
