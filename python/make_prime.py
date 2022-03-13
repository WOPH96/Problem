from itertools import combinations

def isprime(num):
    
    #print(num)
    sq = int(num**(1/2))+1
    print(sq)
    for i in range(2,sq):
        if num%i==0:
            return False
    return True

def solution(nums):
    answer = 0
    for i in combinations(nums,3):
        if isprime(sum(i)):
            answer+=1
    return answer