"""
Question: Find the Nth term of the fibonacci series.
"""



#Without using recursion, i.e. bottom up approach
"""
To run this program, call the bottom_up_approach() with any interger value.
Example: bottom_up_approach(5)
Output:
5

The time complexity of this algorith is O(n).
"""

def bottom_up_approach(N):
  if N==1 or N ==2:
    return 1
  
  fibonacci_array = [None] * (N+1)
  fibonacci_array[0] = 1
  fibonacci_array[1] = 1
  for x in range(2, N+1):
    fibonacci_array[x] = fibonacci_array[N-1] + fibonacci_array[N-2]
  return fibonacci_array[N]


  

#By using recursion
"""
To run this program, call the bottom_up_approach() with any integer value.
Example:
fibo_recursive(5)
Output:
5
"""
def fibo_recursive(N):
  if N==1 or N==2:
    return 1
  return fibo_recursive(N-1) + fibo_recursive(N-2)



