import sys
sys.stdin = open('1987_input.txt','r')

r,c = map(int,input().split())

graph=[]

for i in range(r):
    graph.append(list(input()))
for elem in graph:  
    print(elem)

visited=[[0 for _ in range(c)]for _ in range(r)]

#이미 들어있는지 체크 -> True면 wall이랑 똑같음 
def checkin(ch):
    for row in visited:
        if ch in row:
            return True
    return False

from collections import deque
def bfs(G,v):
    q = deque()
    q.append(v)
    visited[v[0]][v[1]] = G[v[0]][v[1]]
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            #틀에 박지 않았을때만 실행
            if 0<=nx<r and 0<=ny<c:
                # 현재 루틴이 이미 방문 했던 문자가 아니라면
                if not checkin(G[nx][ny]) :
                    visited[nx][ny] = G[nx][ny]
                    q.append((nx,ny))
    pass

bfs(graph,(0,0))
print(visited)
# print(visited[0].count(isinstance(str)))