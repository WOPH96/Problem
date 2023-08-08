import sys
sys.stdin = open('2579_input.txt', 'r')

n = int(input())

steps = [int(input()) for _ in range(n)]

print(steps)

dp = [0]*n
dp[n-1] = steps[n-1]
print(dp)

'''
dp[i]는 그 계단을 밟았을 때 최대의 수
마지막 계단은 무조건 밟아야 하니까.. 거꾸로 진행하는게 나을듯함




'''
