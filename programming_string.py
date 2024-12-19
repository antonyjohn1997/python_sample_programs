#input is :programming
#op will be :progamin


def word_reverse_fn(n):
    demo=""
    for i in n:
        if i not in demo:
            demo+=i

    return demo     

word="programming"
word_reverse=word_reverse_fn(word)
print(word_reverse)
