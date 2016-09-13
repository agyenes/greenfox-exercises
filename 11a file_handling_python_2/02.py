# write a function that takes a filename and returns the number of lines the
# file consists. It should return zero if the file not exists.

def line_counter(file):
    try:
        f = open(file)
        lines = f.readlines()
        i = 0
        for line in lines:
            i += 1
        f.close()
        return i
    except FileNotFoundError:
        print("0")

print(line_counter("01.py"))
print(line_counter("03.py"))
