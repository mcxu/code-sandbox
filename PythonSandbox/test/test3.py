"""
Coin change problem: gives the actual denominations required.
"""
# def solve_coin_change(coins, value):
#     table = [None for x in range(value + 1)]
#     table[0] = []
#     for i in range(1, value + 1):
#         for coin in coins:
#             if coin > i:
#                 continue
#             elif not table[i] or len(table[i - coin]) + 1 < len(table[i]):
#                 if table[i - coin] != None:
#                     print("--- table before: ", table[i])
#                     table[i] = table[i - coin][:]
#                     print("table after: ", table[i])
#                     table[i].append(coin)
#     if table[-1] != None:
#         print('%d coins: %s' % (len(table[-1]), table[-1]))
#     else:
#         print('No solution possible')


def solve_coin_change(coins, value):
    table = [None for x in range(value + 1)]
    table[0] = []
    for i in range(1, value + 1):
        print(f"--- i={i}, table: {table}")
        for coin in coins:
            print("current coin: ", coin)
            if i - coin >= 0 and (not table[i] or len(table[i - coin]) + 1 < len(table[i])):
                if table[i - coin] != None:
                    print("table[i] A: ", table[i])
                    table[i] = table[i - coin][:]
                    print("table[i] B: ", table[i])
                    table[i].append(coin)
                    print("table[i] C: ", table[i])
    
    if table[-1] != None:
        print('%d coins: %s' % (len(table[-1]), table[-1]))
    else:
        print('No solution possible')

# Modify this to alter the denominations of coins
coins = [1, 3, 4]
# coins = [1,5,10,12,25,50]
value = 6
# value = 29
solve_coin_change(coins, value)