def find_substring(s):
    substring=[]
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substring.append(s[i:j])
            
        return substring    
        

string="abc"
result=find_substring(string)
print(result)


def reverse_sentence(sentence):
    # Split the sentence into words
    words = sentence.split()
    
    # Reverse the list of words
    reversed_words = words[::-1]
    print(reversed_words)
    
    # Join the reversed list into a single string
    reversed_sentence = ' '.join(reversed_words)
    
    return reversed_sentence

# Example usage:
sentence = "Hello world from Python"
reversed_sentence = reverse_sentence(sentence)
print(f"The reverse of the sentence is: '{reversed_sentence}'")
