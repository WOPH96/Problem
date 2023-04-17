import sys
sys.stdin = open('11724_input.txt', 'r')

n, m = map(int, input().split())
graph = [[]for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

# graph = list(map(sorted, graph))


def dfs(start):
    # 이미 방문했다면
    if visited[start] == 1:
        return False
    # 방문 안했으면
    else:
        # 방문 처리 후
        visited[start] = 1
        # 인접 노드 전부 방문처리
        for nv in graph[start]:
            dfs(nv)
        return True


cnt = 0
for i in range(1, n+1):
    if dfs(i) == True:
        cnt += 1

print(cnt)
