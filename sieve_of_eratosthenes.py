'''
The sieve of Eratosthenes is preprocessing algorithm that builds an array using which we can efficiently check  if a given number between 
2....n is prime and, if it is not, find one prime factor of the number.
If the last element of the array(sieve) is zero, then the given number is a prime number.
If the last element of the array(sieve) is not zero then the given number is not a prime number. Then the last element is one of the prime factors of the given number.
'''

def sieve_of_eratosthenes(n):
    sieve = [0 for i in range(n-1)]
    for i in range(2, n+1):
        #We use the index i-2 because we check the numbers from 2, but the index of sieve starts from 0.
        if sieve[i-2] !=0:
            continue
        u = i*2
        while u <= n:
            sieve[u-2] = i
            u+=i
    #We use n-2 for the same reason as mentioned above.
    if sieve[n-2] == 0:
        return True
    else:
        return False

num = int(input('Enter the number: '))
is_prime = sieve_of_eratosthenes(num)
if is_prime:
    print('Prime Number')
else:
    print('Not a prime number')
