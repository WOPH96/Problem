import sys
sys.stdin = open('2579_input.txt', 'r')

n = int(input())

steps = [int(input()) for _ in range(n)]

print(steps)

dp = [[0] for _ in range(n)]
print(dp)
# dp[n-1] = steps[n-1]
dp[0] = [steps[0], 0]
print(dp)

'''
dp[i]는 그 계단을 밟았을 때 최대의 수
마지막 계단은 무조건 밟아야 하니까.. 거꾸로 진행하는게 나을듯함
'''

for i in range(1, n):
    if i == 1:

        dp[i] += steps[i]+dp[i-1]
    else:
        dp[i] += max(steps[i-1], steps[i-2])

print(dp)
