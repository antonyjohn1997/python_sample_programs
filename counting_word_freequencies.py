def count_word_frequencies(text):
    words = text.split()  # Split the text into words
    frequency_dict = {}  # Initialize an empty dictionary

    for word in words:
        if word in frequency_dict:
            frequency_dict[word] += 1  # Increment the count if the word is already in the dictionary
        else:
            frequency_dict[word] = 1  # Add the word to the dictionary with a count of 1

    return frequency_dict

# Example usage:
text = "the quick brown fox jumps over the lazy dog"
result = count_word_frequencies(text)
print(result)
