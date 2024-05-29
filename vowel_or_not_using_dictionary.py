def check_vowel_or_consonant(character):

 # a dictionary that act as a swicth-case structure 
    switch={
        'a':'vowel',
        'e':'vowel',
        'i':'vowel',
        'o':'vowel',
        'u':'vowel',
        'A':'vowel',
        'E':'vowel',
        'I':'vowel',
        'O':'vowel',
        'U':'vowel'

        }
    #checking if the character is in the dictionary
    result=switch.get(character,'consonant')#default to 'consonant' if not found
    return result
    
character=input("enter a character:")
if len(character)==1 and character.isalpha():
    result=check_vowel_or_consonant(character)
    print(f"The character '{character}' is a {result}.")
else:
    print("plz enter a single alphabetic character .")
