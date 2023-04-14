# import sys
# sys.stdin = open('2606_input.txt', 'r')

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)

for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

# 오름차순 정렬, 좀 더 나은 방식 찾기
for i in range(1, n+1):
    graph[i].sort()


def PR():
    print(graph)
    print(visited)


def dfs(start):
    if visited[start]:
        return False
    if not visited[start]:
        visited[start] = 1
        for nv in graph[start]:
            dfs(nv)
    return True


dfs(1)
print(visited.count(1)-1)
# PR()
