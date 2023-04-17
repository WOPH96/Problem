from collections import deque
import sys
# sys.stdin = open('7562_input.txt', 'r')
'''
bfs
8칸
'''


def sol():
    def bfs(start, end):
        x, y = start
        # 시작 지점
        visit[x][y] = 1
        q = deque()
        q.append((x, y))
        while q:
            x, y = q.popleft()
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                # 벽이라면
                if not (0 <= nx < l and 0 <= ny < l):
                    continue
                # 이미 방문한 곳이면
                if visit[nx][ny] != 0:
                    continue
                # 다 아니라면 처음 방문한 위치가 된다
                # 이전 방문지점 + 1
                visit[nx][ny] += visit[x][y] + 1
                # 목적지에 도착했다면 더할필요없음
                if (nx, ny) == end:
                    break
                q.append((nx, ny))

    t = int(input())
    for _ in range(t):
        l = int(input())
        visit = [[0 for _ in range(l)]for _ in range(l)]
        start = tuple(map(int, input().split()))
        end = tuple(map(int, input().split()))
        # 나이트 이동범위
        dx = [1, -1, 2, -2, 1, -1, 2, -2]
        dy = [2, 2, 1, 1, -2, -2, -1, -1]
        bfs(start, end)
        print(visit[end[0]][end[1]]-1)


sol()
