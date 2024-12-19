#s="hello"
#reversed_s=s[::-1]
#print(reversed_s)

def reverse_string(s):
    if len(s)<=1:
        return s
    return reverse_string(s[1:]) + s[0]
string="hello"
reversed_string=reverse_string(string)

print(reversed_string)

##########

def reverse_number(num):
    num_str=str(num)
    reversed_str=num_str[::-1]
    reversed_num=int(reversed_str)
    return reversed_num
number=12345
print(reverse_number(number))
