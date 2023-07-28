from collections import deque
import sys
sys.stdin = open('1987_input.txt', 'r')

r, c = map(int, input().split())
M = max(r, c)
graph = []

for i in range(r):
    graph.append(list(input()))
# for elem in graph:
#     print(elem)

res = 0

dx = [1,-1,0,0]
dy = [0,0,1,-1]

history = set()

def dfs(x,y,count):
    global res
    res = max(res,count)
    for i in range(4):
        nx,ny = x+dx[i], y+dy[i]
        if 0<=nx<r and 0<=ny<c and graph[nx][ny] not in history:
                history.add(graph[nx][ny])
                print(graph[nx][ny],history)
                dfs(nx,ny,count+1)
                history.remove(graph[nx][ny])

    pass
history.add(graph[0][0])
dfs(0,0,1)
print(res)




#     print(elem)
# print(visited[0].count(isinstance(str)))
