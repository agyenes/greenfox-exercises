# Create a method that decrypts texts/reversed_zen_order.txt
def decrypt(file_name):
    f = open(file_name)
    lines = reversed(f.readlines())
    new_list = []
    for line in lines:
        new_list += line
    s = ''.join(new_list)
    f.close
    return s

print(decrypt('texts/reversed_zen_order.txt'))
