import sys
sys.stdin = open('15683_input.txt','r')

'''
dfs -> 탐색
cctv위치 
cctv종류에 따른 mode
direction

'''

from copy import deepcopy

#전체 맵
graph=[]
# CCTV 위치
cctv=[[] for _ in range(7)] 

# 벽 위치
wall=[]

N,M = map(int,input().split())
for i in range(N):
    graph.append(list(map(int,input().split())))
    for j in range(M):
        #CCTV 저장
        if 0< graph[i][j] < 6:
            cctv[graph[i][j]].append((i,j))
        elif graph[i][j] == 6:
            wall.append((i,j))
# print(graph)
# for elem in cctv:
#     print(elem)
# print(wall)

#   r,l,d,u  
dx=[0,0,1,-1] # x는 위아래 이동
dy=[1,-1,0,0] # y는 왼오 이동

mode=[
[],
[[0],[1],[2],[3]], # 1번카메라 - r/l/d/u
[[0,1],[2,3]], #2번카메라 - rl/du
[[0,3],[1,2],[1,3],[2,3]], #3번카메라 - ru/ul/ld/dr
[[0,1,2],[0,1,3],[0,2,3],[1,2,3]],#4번카메라 rul,uld,ldr,urd
[[0,1,2,3]],#5번카메라 rldu
]

'''
모드 반복
    모든 cctv반복
or
모든 cctv에 대해
    모든 모드 반복

(0,0)에서 


'''