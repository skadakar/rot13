# ROT13

# ROT13 is a simple letter substitution cipher that replace a letter with the letter 13letters after it in the alphabet.
# Create a function that takes a string and returns the string ciphered with Rot13.
# If there is a number or special character or number it should be returned as is.
import string

# Test strings
test1 = "Nils liker fiskepeniser"
test2 = "Fiskepeniser liker nils"
test3 = "Spesialtegn goes brrrrrrr æøå!!!"
# Test decode
test3encoded = "Fcrfvnygrta tbrf oeeeeeee æøå!!!"


# Individual character conversion
def rot13encodechar(char):
    # Flyttet inn i rot13encodechar siden det ikke trenger være global
    upper = [*string.ascii_uppercase]
    lower = [*string.ascii_lowercase]

    if char in upper:
        charshift = ((upper.index(char)) + 13) % len(upper)
        newchar = upper[charshift]
        return newchar
    if char in lower:
        charshift = ((lower.index(char)) + 13) % len(lower)
        newchar = lower[charshift]
        return newchar
    else:
        return char


# Handling of the string in rot13
def rot13(string):
    finalstring = ""
    for char in string:
        finalstring += (rot13encodechar(char))
    return finalstring


print(rot13(test3))
print(rot13(test3encoded))
