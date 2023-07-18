import sys
sys.stdin = open('1759_input.txt','r')

l,c = map(int,input().split())
alphas = list(input().split())

# print(alphas)

'''
모음 리스트 하나 이상 (aeiou)
자음 리스트 두개 이상

1. 리스트 분리 
    -> aeiou 리스트 만들고, 이 안에 들어가는지만 ㄱ
2. 경우의 수 / 순서 중요 x / combination
모음 리스트 1,모음len까지 / 자음 리스트 c-모음len 만큼 combination 후 리스트 합침

'''

#리스트 분리
aeiou = 'aeiou'
Gathers = [] # 모음 
Consonants = [] # 자음
for alpha in alphas:
    if alpha in aeiou: 
        Gathers.append(alpha)
    else :
        Consonants.append(alpha)
# print(Gathers,Consonants)
# 경우의 수 
from itertools import combinations as cb

res=[] 
#len(consonants)>=2,len(Gaters)>=1
for i in range(1,len(Gathers)+1): # 모음은 최소 한개 
    C = l-i # 자음 뽑아내는 갯수
    if C<2: break 
    for Gather in cb(Gathers,i): #자음은 최소 두개 조건을 넣어야 할듯
        # print(Gather)
        for Consonant in cb(Consonants,C):
            # print(Consonant)
            res_sub = sorted((Gather+Consonant))
            res.append("".join(res_sub))
res.sort()
for elem in res:
    print(elem)