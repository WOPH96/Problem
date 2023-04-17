from collections import deque
import sys
sys.stdin = open('7569_input.txt', 'r')


m, n, h = map(int, input().split())
graph = []
for _ in range(h):
    # z축이 맨 앞
    temp = [list(map(int, input().split())) for _ in range(n)]
    graph.append(temp)
dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


def gr(graph):
    for i in graph:
        for j in i:
            print(j)
        print()
    print()


def bfs(start):
    # 익은 토마토에서 시작
    q = deque()
    for riped in start:
        q.append(riped)
    # print(q/)
    while q:
        # gr(graph)
        z, x, y = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            # 벽이 아닐때만 진행
            if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m:
                # 안익은 토마토일때
                if graph[nz][nx][ny] == 0:
                    # 익는 날짜 추가
                    graph[nz][nx][ny] = graph[z][x][y] + 1
                    # 내일 익는 토마토 큐에 추가
                    q.append((nz, nx, ny))


# 익은 토마토 위치 확인
pos = []
for k in range(h):
    for i in range(n):
        for j in range(m):
            if graph[k][i][j] == 1:
                pos.append((k, i, j))
# print(pos)
bfs(pos)

fail = False

# gr(graph)

MAX = []
for lst in graph:
    for elem in lst:
        if 0 in elem:
            fail = True
            break
    MAX.append(max(map(max, lst)))

if fail:
    print(-1)
else:
    print(max(MAX)-1)
