import sys
sys.stdin = open('9095_input.txt', 'r')

t = int(input())
for _ in range(t):
    n = int(input())
    dp = [0, 1, 2, 4]
    '''
    dp[n]은 n을 만들기 위한 1,2,3의 합
    dp[n] = dp[n-1] + dp[n-2] + dp[n-3]
    '''
    for i in range(4, n+1):
        dp.append(dp[i-3]+dp[i-2]+dp[i-1])
    print(dp[n])
