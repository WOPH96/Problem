import sys
sys.stdin = open('2437_input.txt','r')

n = int(input())
weights = list(map(int,input().split()))

weights.sort()
# print(weights)

'''
0 ~ n 합
0+1 ~ n 까지 합
0+1+2 ~ n 까지 합

set
'''

sums = set()

for i in range(n):
    sums.add(weights[i]) # 추 하나만
    for j in range(i+1,n):
        print(weights[:i+1],weights[j])
        sums.add(sum(weights[:i+1])+weights[j])

print(weights,sums)

for i in range(1,100000000000):
    if i not in sums:
        print(i)
        break

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