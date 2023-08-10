import sys
sys.stdin = open('11053_input.txt','r')

n = int(input())

nums = list(map(int,input().split()))

print(nums)

'''
점화식으로 풀 수 있으면 dp

이전 값이 현재값보다 작다면 카운트 증가

dp[0] = 1
nums[1]<nums[0] -> dp[1] = 1
nums[2]<nums[1]



'''