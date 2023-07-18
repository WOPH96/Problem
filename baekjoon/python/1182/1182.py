import sys
sys.stdin = open('1182_input.txt','r')

n,s = map(int,input().split())

datas = list(map(int,input().split()))
#print(datas)

'''
n < 20 작으니 브루트포스 ㄱㄱ
'''

from itertools import combinations as cb

cnt = 0
for i in range(1,n+1):
    for elem in cb(datas,i):
        if sum(elem) == s :
            cnt+=1
print(cnt)