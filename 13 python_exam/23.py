# Write unittests for this function:

def filter_smaller_than_number(original_list, number):
  if type(original_list) != list:
    return []
  output = []
  for element in original_list:
    if element < number:
      output.append(element)
  return output

# print(filter_smaller_than_number(67.6, 5))
# print(filter_smaller_than_number([2, 5, 7, 9, 11], 10))
# print(filter_smaller_than_number([2, 5, 7, 9, 11], 17))
# print(filter_smaller_than_number([2, 5, 7, 9, 11], 1))
