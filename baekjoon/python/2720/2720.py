import sys
sys.stdin = open('2720_input.txt', 'r')

T = int(input())
casemoney = [int(input()) for _ in range(T)]

coins = [25, 10, 5, 1]
for money in casemoney:
    for coin in coins:
        print(money // coin, end=" ")
        money %= coin
    print()
