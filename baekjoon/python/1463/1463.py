import sys
sys.stdin = open('1463_input.txt', 'r')

n = int(input())

dp = [0, 0, 1, 1]

'''
dp[i] 는, 1로 만들기 위한 연산의 최솟값 
연산
1. 2으로 나누기
2. 3으로 나누기
3. 1을 빼기
'''

for i in range(4, n+1):
    if i % 6 == 0:
        a = 1 + dp[i//2]
        b = 1 + dp[i//3]
        c = 1 + dp[i-1]
        dp.append(min(a, b, c))
    elif i % 2 == 0:
        a = 1 + dp[i//2]
        c = 1 + dp[i-1]
        dp.append(min(a, c))
    elif i % 3 == 0:
        b = 1 + dp[i//3]
        c = 1 + dp[i-1]
        dp.append(min(b, c))
    else:
        dp.append(1 + dp[i-1])

print(dp[n])
