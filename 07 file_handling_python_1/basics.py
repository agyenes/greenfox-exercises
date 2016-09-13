# 1. Create a method that reads all contents of a file when its name given as param
def readfile(file_name):
    f = open(file_name) # ez egy file - ezt kell bezárni!
    r = f.read()
    f.close()
    return r

# 2. Create a method that gets a file_name and a number as param and reads the numberth line of the file
def readline(file_name, number):
    f = open(file_name)
    for i in range(number):
        result = f.readline()
    f.close()
    return result.rstrip()

# 3. Create a method that gets a long sentence as param and gives back the contained words in a list
def words(sentence):
    sentence = sentence[:-1]
    result = sentence.split()
    return result

# 4. Create a method that gets a list of words and creates a sentence with the words separated by spaces
def sentence(words):
    words[-1] = words[-1] + "."
    result = ''
    for word in words:
        result += word + ' '
    result = result[:-1]
    return result

print(sentence(['This', 'is', 'a', 'long', 'sentence']))

# 5. Create a method that gets a string and gives back the character codes in a list
def char_codes(string):
    ch_list = []
    for i in range(len(string)):
        ch_list += [ord(string[i])]
    return ch_list

print(char_codes('almafa'))

# 6. Create a method that gets a list of integers and gives back a string which characters are created from the numbers used as character codes
def string(char_codes):
    new_word = ''
    for i in char_codes:
        new_word += chr(i)
    return new_word

print(string([97, 108, 109, 97, 102, 97]))
