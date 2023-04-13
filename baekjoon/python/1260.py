from collections import deque
# import sys
# sys.stdin = open("1260_input.txt", 'r')


n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)
for i in range(1, n+1):
    graph[i].sort()

# print(graph)


def init():
    global visited
    visited = [0] * (n+1)
    print()


def dfs(start):
    s = []
    s.append(start)
    # visited[start] = 1
    # print(start, end=" ")
    while s:
        # 현재지점
        vertex = s.pop()
        # 방문 했다면
        if visited[vertex]:
            continue
        # 방문하지 않았다면
        if not visited[vertex]:
            visited[vertex] = 1
            print(vertex, end=" ")
            # 주변 노드 방문
            for nv in graph[vertex][::-1]:
                s.append(nv)


def dfs_rcs(start):
    # 방문한 곳이면
    if visited[start]:
        return False
    # 방문 안했으면
    if not visited[start]:
        # 방문처리
        visited[start] = 1
        print(start, end=" ")
        # 주변 노드 방문
        for node in graph[start]:
            dfs_rcs(node)
    return True


def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 1
    print(start, end=" ")
    while q:
        # 현재지점
        vertex = q.popleft()
        # 주변 노드 방문
        for nv in graph[vertex]:
            # 방문 했다면
            if visited[nv]:
                continue
            # 방문하지 않았다면
            if not visited[nv]:
                visited[nv] = 1
                q.append(nv)
                print(nv, end=" ")


# dfs_rcs(v)
# init()
dfs(v)
init()
bfs(v)
init()
# print(graph, visited)


# print(bfs(v))
