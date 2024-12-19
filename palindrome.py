def is_palindrome(sentence):
    # Convert to lowercase and remove spaces
    sentence = sentence.replace(" ", "").lower()
    
    # Reverse the sentence
    reversed_sentence = sentence[::-1]
    
    # Check if the original sentence is equal to the reversed sentence
    return sentence == reversed_sentence

# Example usage:
sentence = "A man a plan a canal Panama"
if is_palindrome(sentence):
    print(f'"{sentence}" is a palindrome.')
else:
    print(f'"{sentence}" is not a palindrome.')
