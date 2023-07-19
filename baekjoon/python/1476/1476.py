import sys
sys.stdin = open('1476_input.txt','r')

E,S,M = map(int,input().split())

'''
1년지날떄마다 esm 1씩 증가
(1 ≤ E ≤ 15, 1 ≤ S ≤ 28, 1 ≤ M ≤ 19)

'''

for i in range(10000):
    cE = i%15+1
    cS = i%28+1
    cM = i%19+1
    # print(cE,cS,cM)
    if (cE==E and cS==S and cM==M):
        break
print(i+1)