import sys
sys.stdin = open('2437_input.txt','r')

n = int(input())
weights = list(map(int,input().split()))

weights.sort()
# print(weights)

'''
idea

target수가 나오기 전까진 모두 만들 수 있음

1 1 2 3 6 7 30

1 < 1
2+1 < 1
3+1 < 2
4+2 < 3
6+3 < 6
9+6 < 7
15+7 <30
22 !  


'''

print(weights)
# for i in range(n):
#     sums.add(weights[i]) # 추 하나만
#     for j in range(i+1,n):
#         print(weights[i:j+1])
#         sums.add(sum(weights[i:j+1]))

# print(weights,sums)

# for i in range(1,100000000000):
#     if i not in sums:
#         print(i)
#         break

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