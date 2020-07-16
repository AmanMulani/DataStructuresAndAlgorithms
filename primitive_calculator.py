'''
You are given a primitive calculator that can perform the following three operations with
the current number 𝑥: multiply 𝑥 by 2, multiply 𝑥 by 3, or add 1 to 𝑥. Your goal is given a
positive integer 𝑛, find the minimum number of operations needed to obtain the number 𝑛
starting from the number 1.

Solution:
We will be using dynamic approach to find out the number of operations.

Example:
Input:
5
Output:
Operations Required: 3
Sequence: 1 2 4 5

Input:
96234
Output:
Operations Required: 14
Sequence: [1, 3, 9, 10, 11, 33, 99, 297, 891, 2673, 8019, 16038, 16039, 48117, 96234]
'''

def number_of_operations(number):

    #initialize an array to hold the number of steps required to reach that number.

    if number == 0:
        print('[]\nNo steps required.')
        quit()
    sequence = []
    operations_array = [0 for i in range(number+1)]
    for i in range(1,number+1):
        operations_array[i] = operations_array[i-1] + 1

        if i%2 == 0:
            operations_array[i] = min(1 + operations_array[i//2], operations_array[i])

        if i%3 == 0:
            operations_array[i] = min(1 + operations_array[i//3], operations_array[i])

    i = number
    while i > 1:
        sequence.append(i)
        if operations_array[i-1] == operations_array[i] - 1:
            i -= 1
        elif i % 2 == 0 and operations_array[i//2] == operations_array[i] - 1:
            i //= 2
        elif i % 3 == 0 and operations_array[i//3] == operations_array[i] - 1:
            i //= 3

    operation_count = len(sequence)
    #including 1 to indicate the start as well.
    sequence.append(1)
    sequence.reverse()
    print('Operations Required:', operation_count)
    print('Sequence:', sequence)
    

try:
    number = int(input('Enter the number: '))
    number_of_operations(number)
except:
    print('Please enter a valid number.')
    quit()

    
