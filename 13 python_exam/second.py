# Create a function that takes a filename and a string as parameter,
# it should write the string to the file 3 times
# example: when called with "tree.txt" and "apple",
# it should write "appleappleapple" to the file "tree.txt".
# the function should not raise an error on any output problem, for example
# denied permission

def write_string_in_file(filename, input_string):
    try:
        file = open(filename, 'w')
        file.write(input_string * 3)
        file.close()
        return file
    except:
        pass

write_string_in_file('tree.txt', 'malna')
write_string_in_file('cccc.txt', 'nagyárpi')
