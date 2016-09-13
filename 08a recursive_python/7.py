# 7. Given a string, compute recursively (no loops) a new string where all the
# lowercase 'x' chars have been changed to 'y' chars.

def x_to_y(string):
    first_letter = string[0]
    if len(string) == 1:
        if string == "x":
            string = "y"
        return string
    else:
        if first_letter == "x":
            first_letter = "y"
        return first_letter + x_to_y(string[1:len(string)])

print(x_to_y("xevlkjhcyyyljhlihxxx"))
