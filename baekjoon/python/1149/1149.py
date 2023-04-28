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
        if i == 0:
            dp[i][j] = t[i][j]
        else:
            # [26,40,83]
            # if j=0 : min(40,83) -> min(a[1],a[2])
            # elif j=1 : min(26,83) -> min(a[0],a[2])
            MIN = 1001
            for k in range(3):
                if k == j:
                    continue
                MIN = min(MIN, dp[i-1][k])
            # print(i, j, MIN)

            dp[i][j] = t[i][j] + MIN
            # print(dp)
            # print(t)
            # print()
print(min(dp[n-1]))
