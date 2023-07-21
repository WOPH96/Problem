import sys
sys.stdin = open('2437_input.txt','r')

n = int(input())
weights = list(map(int,input().split()))

weights.sort()
print(weights)



# from itertools import combinations
# sums=set()
# for i in range(n):
#     for comb in combinations(weights,i):
#        sums.add(sum(comb))
# print(sums)
# for i in range(1,n+1):
#     tmp = (weights[:i])
#     # print(tmp)
#     for comb in combinations(tmp,i-1):
#         print(comb)