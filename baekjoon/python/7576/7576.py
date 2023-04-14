from collections import deque
import sys
sys.stdin = open('7576_input.txt', 'r')


m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def gr(graph):
    for i in graph:
        print(i)
    print()


def bfs(start):
    # 익은 토마토에서 시작
    q = deque()
    for riped in start:
        q.append(riped)
    while q:
        # gr(graph)
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 벽이면
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 안익은 토마토일때만 / 벽 일때, 익은 토마토일때 X
            if graph[nx][ny] == 0:
                # 익는 날짜 추가
                graph[nx][ny] = graph[x][y] + 1
                # 내일 익는 토마토 큐에 추가
                q.append((nx, ny))


fail = False


# 익은 토마토 위치 확인
pos = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            pos.append((i, j))
bfs(pos)

for lst in graph:
    if 0 in lst:
        fail = True
if fail:
    print(-1)
else:
    print(max(map(max, graph))-1)
