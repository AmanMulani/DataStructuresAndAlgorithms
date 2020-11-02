'''
Euclid's algorithm provides an efficient way to find the GCD of two numbers.
gcd(a,b)
    => if(b=0), a
    => else gcd(b, a%b), b!=0
Time complexity: O(log n)

To find the LCM, use the formula:
lcm(a, b) = (a*b) / gcd(a,b)
'''

def gcd(a, b):
    if b==0:
        return a
    return gcd(b, a%b)

a, b = map(int, input('Enter the two numbers: ').split())
print(gcd(a, b))