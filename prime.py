#prime numbers below 100


def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True    

def primes_below(max_num):
    prime_list=[]
    for n in range(2,max_num):
        if is_prime(n):
            prime_list.append(n)
    return prime_list    
prime_numbers=primes_below(100)
print(prime_numbers)
