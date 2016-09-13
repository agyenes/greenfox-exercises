# Create a function that takes a filename as string parameter,
# and counts the occurances of the letter "a", and returns it as a number.
# It should not break if the file not exists just return 0

def count_a_in_file_content(filename):
  try:
    content = get_content_from_file(filename)
  except:
    return 0
  count = 0
  for char in content:
    if char == 'a':
      count += 1
  return count

def get_content_from_file(filename):
  file = open(filename, 'r')
  content = file.read()
  file.close()
  return content
