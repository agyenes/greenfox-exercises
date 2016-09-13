# Create a function that takes a filename as parameter,
# it should count the words in the file and is should return it as a number
# if the file not exists or any other error occures return 0

def count_words_in_file_content(filename):
  try:
    content = get_content_from_file(filename)
  except:
    return 0
  count = 0
  for word in content.split(' ')[:-1]:
    count += 1
  return count

def get_content_from_file(filename):
  file = open(filename, 'r')
  content = file.read()
  file.close()
  return content

print(count_words_in_file_content('lorem.txt'))
