"""
Question: Find the Nth term of the fibonacci series.
"""



#Without using recursion, i.e. bottom up approach

def bottom_up_approach(N):
  if N==1 or N ==2:
    return 1
  
  fibonacci_array = [None] * (N+1)
  fibonacci_array[0] = 1
  fibonacci_array[1] = 1
  for x in range(3, N+1):
    fibonacci_array[x] = fibonacci_array[N-1] + fibonacci_array[N-2]
  return fibonacci_array[N]
  
