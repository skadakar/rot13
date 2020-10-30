#Rot13 made universal with rot level up to the user.

import string

# Test strings
test1 = "Nils liker fiskepeniser"
test2 = "Fiskepeniser liker nils"
test3 = "Spesialtegn goes brrrrrrr æøå!!!"
# Test decode
test3encoded = "Fcrfvnygrta tbrf oeeeeeee æøå!!!"



# Individual character conversion
def rotencodechar(char,rotlevel):

    #Flyttet inn i rot13encodechar siden det ikke trenger være global
    upper = [*string.ascii_uppercase]
    lower = [*string.ascii_lowercase]

    if char in upper:
        charshift =  ((upper.index(char)) + rotlevel) % len(upper)
        newchar = upper[charshift]
        return newchar
    if char in lower:
        charshift =  ((lower.index(char)) + rotlevel) % len(lower)
        newchar = lower[charshift]
        return newchar
    else:
        return char

# Handling of the string in rot13
def rot(string, rotlevel):
    finalstring =""
    for char in string:
        finalstring += (rotencodechar(char, rotlevel))
    return finalstring

def derot(string, rotlevel):
    finalstring =""
    for char in string:
        finalstring += (rotencodechar(char, -rotlevel))
    return finalstring

print(rot(test3,13))
#print(rot(test3encoded,13))

print(rot(test3,10))
print(derot("Czocskvdoqx qyoc lbbbbbbb æøå!!!", 10))

