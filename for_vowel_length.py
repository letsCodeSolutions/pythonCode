vowel = 0
consonent = 0
numbers = 0
for letter in "Manish Singh 01":
    if letter.lower() in "aeiou":
        vowel = vowel + 1
    elif letter == '':
        pass
    elif letter in "0123456789":
        numbers = numbers + 1
    else:
        consonent = consonent + 1

print("Vowel count {}".format(vowel))
print("Consonent count {}".format(consonent))
print("Number count {}".format(numbers))
    
