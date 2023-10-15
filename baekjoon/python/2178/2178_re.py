from collections import deque
import sys

sys.stdin = open("2178_input.txt", "r")

# 최단거리 bfs

n,m = map(int,input().split())
# print(n,m)

graph=[list(map(int,input())) for _ in range(n)]

# for elem in graph:
#     print(elem)

def bfs(sx,sy):
    q = deque()
    q.append((sx,sy))
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    while q:
        x,y= q.popleft()
        for i in range(4):
            nx, ny = x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y]+1
                    q.append((nx,ny))

bfs(0,0)

# for elem in graph:
#     print(elem)

print(graph[n-1][m-1])