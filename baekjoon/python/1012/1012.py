from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)
sys.stdin = open('1012_input.txt', 'r')


def sol():
    def print_graph(graph):
        for row in graph:
            print(row)
        print()

    def dfs_rcs(graph, x, y):
        if x < 0 or x >= n or y < 0 or y >= m:
            return False
        if graph[x][y] == 0:
            return False
        if graph[x][y] == 1:
            # print_graph(graph)
            graph[x][y] = 0
            dfs_rcs(graph, x-1, y)
            dfs_rcs(graph, x+1, y)
            dfs_rcs(graph, x, y-1)
            dfs_rcs(graph, x, y+1)
        return True

    def dfs(graph, x, y):
        # 배추 없으면
        if graph[x][y] == 0:
            return False
        # 배추 있으면
        if graph[x][y] == 1:
            graph[x][y] = 0
            s = []
            s.append((x, y))
            dx = [0, 0, 1, -1]
            dy = [1, -1, 0, 0]
            while s:
                x, y = s.pop()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < m:
                        if graph[nx][ny] == 0:
                            continue
                        if graph[nx][ny] == 1:
                            s.append((nx, ny))
                            graph[nx][ny] = 0
            return True

    t = int(input())
    for _ in range(t):
        bug = 0
        n, m, k = map(int, input().split())
        graph = [[0 for _ in range(m)] for _ in range(n)]
        for _ in range(k):
            x, y = map(int, input().split())
            graph[x][y] = 1

        # print_graph(graph)
        for i in range(n):
            for j in range(m):
                if dfs(graph, i, j) == True:
                    bug += 1
        print(bug)


sol()
