'''
Merge Sort
Time Complexity: O(nlogn)
'''

def merge_sort(A, start_index, end_index):
    if(start_index < end_index):
        mid_index = (start_index + end_index) // 2
        merge_sort(A, start_index, mid_index)
        merge_sort(A, mid_index + 1, end_index)
        merge(A, start_index, mid_index, end_index)

def merge(A, start_index, mid_index, end_index):

    # print('INSIDE MERGE METHOD')
    # print('Array:', A)
    # print('Start Index:', start_index)
    # print('Mid Index:', mid_index)
    # print('End Index:', end_index)
    

    n1 = mid_index - start_index + 1
    n2 = end_index - mid_index 
    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(n1):
        L[i] = A[start_index+i]
    
    for j in range(n2):
        R[j] = A[mid_index + 1 + j]

    # print(L)
    # print(R)
    i = 0 
    j = 0
    k = start_index
    while i<n1 and j<n2:
        if L[i] <= R[j]:
            A[k] = L[i]
            i+=1
        else:
            A[k] = R[j]
            j+=1
        k+=1
    
    while i < n1:
        A[k] = L[i]
        i+=1
        k+=1

    while j < n2:
        A[k] = R[j]
        j+=1
        k+=1

    print("="*35)


input_array = [20, 19, 18, 17, 205, 16, 15, 14, 13, 12, 366, 11, 10, 21, 25, 27, 29, 28, 9, 8, 6, 5, 4, 7, 3, 2, 1, 0]
merge_sort(input_array, 0, len(input_array)-1)
print(input_array)