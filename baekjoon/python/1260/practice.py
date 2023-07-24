from collections import deque
import sys
sys.stdin = open("1260_input.txt", 'r')

n, m, v = map(int, input().split())

graph = [[]for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for elem in graph:
    elem.sort()
    print(elem)
# print(graph)


def dfs_rec(G, vt):
    if visited[vt]:
        return
    else:
        visited[vt] = True
        print(vt, end=" ")
        for nv in G[vt]:
            dfs_rec(G, nv)


def dfs_stack(G, vt):
    s = []
    s.append(vt)
    while s:
        now = s.pop()
        if not visited[now]:
            visited[now] = True
            print(now, end=" ")
            for nv in G[now][::-1]:
                s.append(nv)
    print()


def bfs(G, vt):
    q = deque()
    q.append(vt)
    while q:
        now = q.popleft()
        if not visited[now]:
            visited[now] = True
            print(now, end=" ")
            for nv in G[now]:
                q.append(nv)
    print()


visited = [False] * (n+1)
dfs_rec(graph, v)
print()
visited = [False] * (n+1)
dfs_stack(graph, v)
visited = [False] * (n+1)
bfs(graph, v)
