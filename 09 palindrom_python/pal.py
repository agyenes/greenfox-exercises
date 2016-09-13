#Create a function that takes a string and creates a palindrome from it. It should work like this:

def create_palindrome(input):
    string2 = ''
    for i in range(1, len(input) + 1):
        string2 += input[len(input) - i]
    return str(string2)

output = create_palindrome('pear')

print(output)
