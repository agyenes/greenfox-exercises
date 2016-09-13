# Create a method that decrypts the texts/duplicated_chars.txt

def decrypt(file_name):
    f = open(file_name)
    new_list = []
    lines = f.readlines()
    for line in lines:
        if line != '':
            new_list += line[::2]
    s = ''.join(new_list)
    f.close()
    return s

print(decrypt('texts/duplicated_chars.txt'))
