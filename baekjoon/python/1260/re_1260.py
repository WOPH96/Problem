import sys
sys.stdin = open("1260_input.txt", 'r')

'''
dfs
bfs

양방향
'''

n,m,v = map(int,input().split())

graph=[[] for _ in range(n+1)]
# [ [0] 간선
#  [1]
#  [2]
# print(graph)
for i in range(m):
    a,b = map(int,input().split())
    # 양방향
    graph[a].append(b)
    graph[b].append(a)

for elem in graph:
    elem.sort()

print(graph)

from collections import deque

visited=[False]*(n+1)

def dfs_rec(G,v):
    pass

def dfs_stack(G,vertex):
    s = []
    s.append(vertex)
    while s:
        out = s.pop()
        if not visited[out] :
            visited[out] = True
            print(out,end=" ")
            #거꾸로 넣기
            for nv in G[out][::-1]:
                s.append(nv)
        else 
            continue
    print()

def bfs(G,v):
    pass

dfs_stack(graph,v)