import sys
sys.stdin = open('1427_input.txt', 'r')

nums = list(input())
nums.sort(reverse=True)
print("".join(nums))
