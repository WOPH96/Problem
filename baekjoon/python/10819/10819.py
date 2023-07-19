import sys
sys.stdin = open('10819_input.txt','r')

'''
MAX <- |A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|
'''

n = int(input())
datas=list(map(int,input().split()))
# print(datas)

M = 0

from itertools import permutations

for elem in permutations(datas,n):
    sum=0
    for i in range(n-1):
        sum+=abs(elem[i]-elem[i+1])
        M=max(M,sum)
print(M)