# 9. Given a string, compute recursively a new string where all the
# adjacent chars are now separated by a "*".

def add_star(string):
    first_letter = string[0]
    if len(string) == 1:
        new_string = first_letter + "*"
        return new_string
    else:
        new_string = first_letter + "*"
        return new_string + add_star(string[1:len(string)])

print(add_star("xsdlcjasluchdasx"))
