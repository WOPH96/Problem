# 개수가 적은 친구부터 픽

def solution(nums):
    answer = 0
    able = len(nums)//2
    nums.sort(reverse=True)
    
    select = set()
    
    while len(select)!=able and nums:
        select.add(nums.pop())
    
    return len(select)