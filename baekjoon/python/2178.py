from collections import deque
# import sys

# sys.stdin = open("2178_input.txt", "r")

# 최단거리 bfs
# 시작위치, 도착위치 포함 2번째 칸은 거리 2라는 뜻
n, m = map(int, input().split())

load = []

for i in range(n):
    load.append(list(map(int, input())))

# 출발위치 - 0,0 이고, 목적위치 n-1,m-1인 것을 기억
# 벽 0, 길 1


def bfs(x, y):
    q = deque()
    q.append((x, y))
    # 이동범위
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 공간 밖이라면
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 길이 아니라면
            if load[nx][ny] == 0:
                continue
            # 길이라면
            if load[nx][ny] == 1:
                # 현재 경로 + 1 추가한 거리
                q.append((nx, ny))
                load[nx][ny] = load[x][y] + 1

    print(load[n-1][m-1])


bfs(0, 0)
