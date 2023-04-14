from collections import deque
import sys
sys.stdin = open('1012_input.txt', 'r')

# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]

# m = n = k = 0


# def bfs(graph, x, y):
#     # 입력받은게 배추없는 땅이면 탐색X
#     if graph[x][y] == 0:
#         return False
#     q = deque()
#     q.append((x, y))
#     while q:
#         x, y = q.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or nx >= n or ny < 0 or ny >= m:
#                 continue
#             if graph[nx][ny] == 0:
#                 continue
#             if graph[nx][ny] == 1:
#                 graph[nx][ny] = 1
#                 q.append((nx, ny))
#     return True

m = n = k = 0


def dfs_rcs(graph, x, y):
    if x < 0 or x >= m or y < 0 or y >= n
    if graph[x][y] == 0:
        return False
    if graph[x][y] == 1:
        dfs_rcs(graph, x)


def sol():
    t = int(input())
    for _ in range(t):
        bug = 0
        m, n, k = map(int, input().split())
        graph = [[0 for _ in range(n)] for _ in range(m)]
        for _ in range(k):
            x, y = map(int, input().split())
            graph[y][x] = 1

        # print(graph)
        for i in range(n):
            for j in range(m):
                if dfs_rcs(graph, y, x) == True:
                    bug += 1
        print(bug)


sol()
