# 8. Given a string, compute recursively a new string where all the 'x' chars have been removed.

def x_to_y(string):
    first_letter = string[0]
    if len(string) == 1:
        if string == "x":
            string = ""
        return string
    else:
        if first_letter == "x":
            first_letter = ""
        return first_letter + x_to_y(string[1:len(string)])

print(x_to_y("xevlkjhcyyyljhlihxxx"))
