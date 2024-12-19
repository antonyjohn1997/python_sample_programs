def are_anagrams(s1,s2):
    s=sorted(s1)
    print(s)
    u=sorted(s2)
    print(u)
    return sorted(s1)==sorted(s2)

s1="listen"
s2="silent"
result=are_anagrams(s1,s2)
print(result)
