# Create a function that searches for all the palindromes in a string that are at least than 3 characters, and returns a list with the found palindromes. Example:

def search_palindromes(input_string):
    p_list = []                                                     #lista kezdetben üres
    for str_len in range(3, len(input_string)):                     #a ciklus olyan stringeket keres, amelyek hossza 3 és az input hossza között van
        for i in range(0, len(input_string) - (str_len-3)):         #végigfut az elemeken nullától az input hosszának megfelelő elemig
            first = i                                               #vizsgált string kezdete, először 0
            last = first + str_len                                  #vizsgált string vége, először 3, aztán nő
            seq = input_string[first:last]                          #vizsgált string a fenti két paraméter alapján
            if seq == seq[::-1]:                                    #megvizsgálja h az első és az utolsó elemek megegyeznek -e
                p_list.append(seq)                                  #ha igen, berakja a listába
    return p_list                                                   #visszaadja a kész listát

print("-I, the royal we, you know, the editorial, I dropped off the görög money, exactly as per, Look, man I've got certain information integetni alright? Certain things have come to light, and uh, ya know, has it ever occurred to you, that uh, instead of uh, you know running around, uh uh, blaming me, given the nature of all this new shit, you know it, it it, this could be a uh, a lot more uh, uh, uh, uh, complex, I mean it's not just, it might not be, just such a simple, uh, you know?")
print("")
print(search_palindromes("-	I, the royal we, you know, the editorial, I dropped off the görög money, exactly as per, Look, man I've got certain information integetni alright? Certain things have come to light, and uh, ya know, has it ever occurred to you, that uh, instead of uh, you know running around, uh uh, blaming me, given the nature of all this new shit, you know it, it it, this could be a uh, a lot more uh, uh, uh, uh, complex, I mean it's not just, it might not be, just such a simple, uh, you know?"))
