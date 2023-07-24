from collections import deque
import sys
sys.stdin = open("2178_input.txt", "r")

n, m = map(int, input().split())

graph = []

for i in range(n):
    ith_row = list(map(int, input()))
    graph.append(ith_row)
    print(ith_row)

'''
1은 통과 0은 벽
최단거리 bfs
이동은 상하좌우로 ㄱㄱ
이동했을때 그래프가 1이면 -> 한번도 안가본 길
    기존 경로에 플러스
'''


def bfs(G, v):
    q = deque()
    q.append(v)
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            if G[nx][ny] == 0:
                continue
            elif G[nx][ny] == 1:
                G[nx][ny] += G[x][y]
                q.append((nx, ny))
                print()
                for elem in G:
                    print(elem)


bfs(graph, (0, 0))

print()
for elem in graph:
    print(elem)
