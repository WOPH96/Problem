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
    pass

bfs(graph,(0,0))
# print(visited[0].count(isinstance(str)))