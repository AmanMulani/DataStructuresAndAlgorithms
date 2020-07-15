'''
The problem statement is to find the minimum number of coins required to sum up the given amount.
Denominations are provided by the users.
To find the number of coins required, we will be using dynamic approach. Greedy approach is used to verify whether the 
denomination provided can sum upto the given amount.

Ex:
Input:
Enter the amount: 15
Enter coin denominatios: 1 5 7
Output:
Required number of coins:  3

Input:
Enter the amount: 47
Enter coin denominatios: 2 4 6
Output:
Denominations cannot sum upto the given amount
'''


def money_change(money, coin_denominations):
    coin_denominations.sort()
    list_of_coins = []
    #finding
    min_number_coins = [0 for i in range(money+1)]
    for i in range(1, money+1):
        min_number_coins[i] = money
        for coin in coin_denominations:
            if i>=coin:
                num_coins = min_number_coins[i - coin] + 1
                if num_coins < min_number_coins[i]:
                    min_number_coins[i] = num_coins
    amount = money
    count = 0
    index = len(coin_denominations)-1
    #Using the greedy approach to verify whether the number of coins sum up to the given amount.
    for i in range(min_number_coins[money]):
        if index<0:
            break
        if amount % coin_denominations[index] == 0:
            coins = (amount // coin_denominations[index])
            i -= coins
            count += coins
            amount = amount%coin_denominations[index]
            index -= 1
            break
        elif amount > coin_denominations[index]:
            coins = (amount // coin_denominations[index])
            i -= coins
            amount = amount%coin_denominations[index]
            count += coins
            index -= 1
            continue
        else:
            index -= 1
            continue
    if amount != 0:
        return False
    return min_number_coins[money]

try:
    amount = int(input('Enter the amount: '))
    denominations = list(map(int, input('Enter coin denominatios: ').split()))
    coins = money_change(amount, denominations)
    if coins == False:
        print('Denominations cannot sum upto the given amount')
    else:
        print('Required number of coins: ', coins)
except:
    print('Please enter valid numbers.')
    quit()