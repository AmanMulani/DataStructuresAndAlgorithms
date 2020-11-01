'''
A program to find whether the given number is prime or not.
Time Complexity: O(sqrt(n))
'''
def primeNumber(n):
    if n<2:
        return False
    i = 2
    while i*i <= n:
        if n%i == 0:
            return False
        i += 1
    return True

print('Enter the number')
num = int(input())
if primeNumber(num):
    print('The given number is a prime')
else:
    print('The given number is not a prime')