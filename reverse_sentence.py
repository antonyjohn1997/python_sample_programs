#Given a sentence, reverse the order of the words but keep the words themselves unchanged.
#For example, given the #input sentence "The quick brown fox", the output should be
#"fox brown quick The"

def get_words(n):
    words=n.split()
    #print(words)
    reverse=words[::-1]
    #print(reverse)
    reversed_form=' '.join(reverse)
    return reversed_form    
sentence="The quick brown box"
get_reversed_sentence=get_words(sentence)
print(get_reversed_sentence)
