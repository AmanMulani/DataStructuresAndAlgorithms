'''
A program to find out the prime factors of the given number
'''

def prime_factors(n):
    #if you just want unique factors use set instead of list.
    prime_factors_list = []
    i = 2
    while i*i <= n:
        while n%i == 0:
            prime_factors_list.append(i)
            n //= i 
        i += 1
    
    if n > 1:
        prime_factors_list.append(n)

    return prime_factors_list

num = int(input('Please enter the number: '))
print('The prime factors are:', prime_factors(num))