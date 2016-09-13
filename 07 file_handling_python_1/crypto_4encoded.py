# Create a method that decrypts texts/encoded_zen_lines.txt
def decrypt(file_name):
    f = open(file_name)
    lines = f.readlines()
    new_list = []
    for i in lines:
        for c in i:
            if c == ' ' or c == '\n':
                new_list.append(c)
            else:
                decr = ord(c) - 1
                encr = chr(decr)
                new_list.append(encr)
    s = ''.join(new_list)
    f.close
    return s

print(decrypt('texts/encoded_zen_lines.txt'))
