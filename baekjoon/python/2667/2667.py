import sys
sys.stdin = open('2667_input.txt', 'r')

n = int(input())

graph = [list(map(int, input())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def PR():
    print(graph)
    # print(visited)


def dfs(x, y):
    s = []
    s.append((x, y))
    house = 0
    while s:
        # 현 위치
        x, y = s.pop()
        # 집 없으면 찾을필요 없음
        if graph[x][y] == 0:
            continue
        # 집 있으면
        if graph[x][y] == 1:
            # 집 카운트, 주변에 있는 집 샅샅이 뒤지기
            house += 1
            graph[x][y] = 0

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # 벽이면
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if graph[nx][ny] == 0:
                    continue
                if graph[nx][ny] == 1:
                    s.append((nx, ny))
    return house


def sol():
    housing = []
    danzi = 0
    for i in range(n):
        for j in range(n):
            house = dfs(i, j)
            if house != 0:
                housing.append(house)
                danzi += 1
    print(danzi)
    housing.sort()
    for h in housing:
        print(h)


sol()
