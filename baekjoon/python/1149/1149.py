import sys
sys.stdin = open('1149_input.txt', 'r')

n = int(input())

dp = [[0 for _ in range(3)] for _ in range(n)]
t = []
for _ in range(n):
    t.append(list(map(int, input().split())))

'''
재귀함수로 구현 어떻게 할지 구상
'''
for i in range(n):
    for j in range(3):
        MIN=1000
        if i == 0 :
            dp[i][j] = t[i][j]
        else:
            MIN = min(MIN,)

            
                
        