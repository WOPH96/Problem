import sys
sys.stdin = open('4963_input.txt', 'r')


def sol():
    def dfs(x, y):
        # 바다라면
        if graph[x][y] == 0:
            return False
        # 섬이라면 주변 섬 전부 찾아내, 이미 찾았으므로 True
        s = []
        s.append((x, y))
        graph[x][y] = 0
        while s:
            x, y = s.pop()
            for i in range(8):
                # 상하좌우 대각선까지 찾아
                nx = x + dx[i]
                ny = y + dy[i]
                # 벽 밖으로 나가면
                if not (0 <= nx < h and 0 <= ny < w):
                    continue
                # 이미 바다면
                if graph[nx][ny] == 0:
                    continue
                # 두 조건 다 아니면 섬이다, 방문처리
                graph[nx][ny] = 0
                s.append((nx, ny))
                # print(s)
        return True

    while True:
        w, h = map(int, input().split())
        if w == 0 and h == 0:
            break
        graph = []
        for _ in range(h):
            graph.append(list(map(int, input().split())))
        # print(graph)
        dx = [0, 0, 1, -1, 1, 1, -1, -1]
        dy = [1, -1, 0, 0, 1, -1, 1, -1]
        land = 0
        for i in range(h):
            for j in range(w):
                if dfs(i, j) == True:
                    land += 1
        print(land)


sol()
