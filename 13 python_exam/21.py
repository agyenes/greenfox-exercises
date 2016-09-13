# Create a function that takes a list as a parameter,
# and returns a boolean it should return True if none of the elements are
# even, False otherwise
# It should raise an error if the parameter is not a list

def even_elements_investigator(original_list):
  if type(original_list) != list:
    raise TypeError('The argument is not a list')
  output = []
  num = 0
  for num in original_list:
    if num % 2 == 0:
      return False
      break
  else:
      return True
