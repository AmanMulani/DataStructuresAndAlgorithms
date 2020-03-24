"""
Question: Find the Nth term of the fibonacci series.
"""



#Without using recursion, i.e. bottom up approach
"""
To run this program, call the bottom_up_approach() function with any interger value.
Example: 
print(bottom_up_approach(5))
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
To run this program, call the bottom_up_approach() function with any integer value.
Example:
print(fibo_recursive(5))
Output:
5
"""
def fibo_recursive(N):
  if N==1 or N==2:
    return 1
  return fibo_recursive(N-1) + fibo_recursive(N-2)


#By using dynamic programming, memoized solution
"""
To run this program, call the finonacci() function with an integer value.
Example:
print(fibonacci(5))
Output:
5
"""

def fibonacci_memoized(N, memo):
  if memo[N] != null:
    return memo[N]
  else if N==1 or N==2:
    result = 1
  elif:
    result = fibonacci_memoized(N-1, memo) + fibonacci_memoized(N-2, memo)
  memo[N] = result
  return result

def fibonacci(N):
  return fibonacci_memoized(N, [None]*(N+1))
    
