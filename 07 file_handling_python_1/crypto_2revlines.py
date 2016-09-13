# Create a method that decrypts texts/reversed_zen_lines.txt

def decrypt(file_name):
    f = open(file_name)
    lines = f.readlines()
    new_list = []
    for line in lines:
        new_list += line[::-1][1:]
        new_list += '\n'
    s = ''.join(new_list)
    f.close
    return s

print(decrypt('texts/reversed_zen_lines.txt'))
