#character=input("enter a character : ")
#vowels=['a','e','i','o','u','A','E','I','O','U']# created a vowels list 
#if character in vowels:
    #print(f"the character '{character}' is a vowel")
#else:
    #print(f"the character '{character}' is a consonant")

#using function

def isVowel(char):
    vowels="aeiouAEIOU" #creating string of vowels
    if vowels.find(char)!=-1:
        print(f"the charcter '{char}' is a vowel ")
    else:
        print(f"the charcter '{char}' is a consonant")
character=input("enter character:")
isVowel(character)


        
    
