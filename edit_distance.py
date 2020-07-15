'''
Edit distance is the minimum number of operations needed to change one string to another.
The allowed number of operations are:
Insertion, Deletion and Transition.
'''

def editDistance(string1, string2):

    #Define a two dimensional matrix
    wordMatrix = [[0 for i in range(len(string1)+1)] for j in range(len(string2) + 1)]
    
    for i in range(len(string1)+1):
        wordMatrix[0][i] = i
    
    for j in range(len(string2) + 1):
        wordMatrix[j][0] = j

    print('Before starting the edit distace problem--->>>')
    print('\t'*2, end = "")
    for i in range(len(string1)):
        print(string1[i], '\t', end = "")
    print()

    for j in range((len(string2)+1)):
        if j != 0:
            print(string2[j-1], '\t', end = "")
        else:
            print('\t', end = '') 
        for i in range(len(string1) + 1):
            print(wordMatrix[j][i], '\t', end = "")
        print()
 
    print('------------------------------------------------------------------------------------')
    
    for j in range(1, len(string2)+1):
        for i in range(1, len(string1)+1):
            if string1[i-1] == string2[j-1]:
                wordMatrix[j][i] = wordMatrix[j-1][i-1]
            else:
                wordMatrix[j][i] = min(wordMatrix[j-1][i], wordMatrix[j][i-1], wordMatrix[j-1][i-1]) + 1

    print('Final Result---->>>>')
    print('\t'*2, end = "")
    for i in range(len(string1)):
        print(string1[i], '\t', end = "")
    print()

    for j in range((len(string2)+1)):
        if j != 0:
            print(string2[j-1], '\t', end = "")
        else:
            print('\t', end = '') 
        for i in range(len(string1) + 1):
            print(wordMatrix[j][i], '\t', end = "")
        print()
 
    print('------------------------------------------------------------------------------------')


    return wordMatrix[len(string2)][len(string1)]
    



inp = input('Enter string1: ')
inp2 = input('Enter string2: ')

print(editDistance(inp.upper(), inp2.upper()))
