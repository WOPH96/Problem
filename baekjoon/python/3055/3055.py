import sys
sys.stdin = open('3055_input.txt','r')

n, m = map(int,input().split())

graph=[]
visited=[[False]*m for _ in range(n)]
pos_D = []
pos_S = []
pos_W = []

for i in range(n):
    tmp = list(input())
    if 'D' in tmp:
        pos_D.append([i,tmp.index('D')])
    if 'S' in tmp:
        pos_S.append([i,tmp.index('S')])
    if '*' in tmp:
        Ws =[[i,j] for j,x in enumerate(tmp) if x in "*"]
        pos_W.extend(Ws)
    graph.append(tmp)


# print(pos_D)
# print(pos_S)
# print(pos_W)


'''
물 먼저 채우고, 비버 이동시키기
물은 매 분 사방으로 이동 -> 매번 동일하게 변경 -> bfs로 ㄱㄱ
비버는 매 분 한 방향으로 이동 가능 -> dfs로 ㄱㄱ

'''

from collections import deque

dx=[1,-1,0,0]
dy=[0,0,1,-1]

'''
한 턴 끝날떄마다, 전파시킨 좌표를 리턴한다면?
'''
from copy import deepcopy

def flood_bfs(G,q):
    rq = deque()
    _graph=G
    while q: 
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if _graph[nx][ny]=='.':
                    _graph[nx][ny]='*'
                    rq.append((nx,ny))
    return rq
'''
비버의 위치를 받아서
dfs
물 차는 그래프랑 같이 전송
'''

def move_dfs(G,v,que):
    a,b = v[0]
    visited[a][b]=True
    s = [[G,que,visited,0,a,b]]
    repeat=0
    while s:
        repeat+=1
        Gr,q,_visit,cnt,x,y = s.pop()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                graph=deepcopy(Gr)
                que=deepcopy(q)
                visit=deepcopy(_visit)
                if graph[nx][ny]=='D':
                    print("GET")
                    return cnt+1
                elif graph[nx][ny]=='.' and not visit[nx][ny]:
                    #이동하고
                    graph[nx][ny]='S'
                    graph[x][y]='.'
                    #홍수 범람
                    # 
                    # print(que)
                    print(f"{x,y}->{nx,ny}이동, 현재 cnt={cnt+1}")
                    for elem in graph:
                        print(elem)
                    que = flood_bfs(graph,que)
                    print(que)
                    print(f"{nx,ny}이동하고나서 홍수, 현재 cnt={cnt+1}")
                    for elem in graph:
                        print(elem)
                    print()
                    s.append((graph,q,visit,cnt+1,nx,ny))
        # if repeat>3:
        #     break            


                #     graph[nx][ny]='*'
                #     rs.append((nx,ny))
    return -1

# print(pos_W.pop())

#초기 홍수
print("맨처음")
for elem in graph:
    print(elem)
print()
que = flood_bfs(graph,deque(pos_W))
#초기 비버
print("홍수 1번 난 이후")
for elem in graph:
    print(elem)
print()


print(move_dfs(graph,pos_S,que))
