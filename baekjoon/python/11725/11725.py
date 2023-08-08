from collections import deque
import sys
sys.stdin = open('11725_input.txt', 'r')

n = int(input())

graph = [[] for _ in range(n+1)]

print(graph)

for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(graph)

visited = [False]*(n+1)
parent = [0]*(n+1)


def bfs(root):
    q = deque()
    q.append(root)
    while q:
        p = q.popleft()
        if not visited[p]:
            visited[p] = True
            for nv in graph[p]:
                parent[nv] = p
                q.append(nv)


bfs(1)
print(parent)
