def vowel_indices(word):
    new_list = []
    for char in word:
        if char in 'aeiouAEIOU':
            new_list += [word.index(char) + 1]
            word.replace('char', ' ')
    return new_list

print(vowel_indices('supeueueueuer'))

str = "this is string example....wow!!! this is really string";
print(str.replace("is", "was"))
