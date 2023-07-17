import sys
sys.stdin = open('14502_input.txt', 'r')

n,m = map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))

# for elem in graph:
#     print(elem)

'''
벽세우기 완탐
바이러스침공 bfs으로 진행

0공간에 (safe)다가 벽 3개 세우기
최대공간 나오는거 뽑아내기

'''

# 빈공간 / 바이러스 존 기록
safe_zone =[]
virus_zone = []
for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            safe_zone.append((i,j))
        elif graph[i][j]==2:
            virus_zone.append((i,j))

# print(safe_zone,virus_zone,sep="\n")
# print()

# 복사된 맵에서 바이러스 퍼뜨리기 (시뮬레이션)
# 0공간 확인
M = 0
from collections import deque
def BFS(graph):
    global M
    # 안전구역 카운트, 바이러스가 침공할때마다 줄어듦
    safe_cnt = len(safe_zone)-3
    # BFS를 위한 바이러스 queue 생성
    q = deque()
    for virus in virus_zone:
        q.append(virus)
    # 바이러스는 상하좌우로 퍼지므로 움직임 생성
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    #바이러스 퍼짐 시작
    while (q):
        x,y= q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #움직인 범위가 틀을 넘었다면 다시
            if not(0<=nx<n and 0<=ny<m):
                continue
            #움직인 곳이 벽이라면 다시
            if graph[nx][ny]==1:
                continue
            #움직인 곳이 빈공간이라면 침투
            if graph[nx][ny]==0:
                graph[nx][ny]=2
                q.append((nx,ny))
                safe_cnt-=1
            #움직인 곳이 바이러스 인 경우는 아예 취급 안함, 중복제거
    M = max(M,safe_cnt)
            
    
#빈공간에 벽 3개 설치
#벽 3개 쳐진 경우의 수 중에 가장 공간 확보 많이된 경우를 구하는 것
from itertools import combinations as cb

for combo in cb(safe_zone,3):
    #벽 3개 치고 바이러스 퍼뜨리기 -> BFS -> 개수 리턴
    import copy
    tmp_graph = copy.deepcopy(graph)
    for wi,wj in combo: # wall 생성
        tmp_graph[wi][wj] = 1
    BFS(tmp_graph)
    # for elem in tmp_graph:
    #     print(elem)
    

print(M)
