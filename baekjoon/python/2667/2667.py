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
    s.append(x, y)
    while s:
        x, y = s.pop()


def sol():
    housing = []
    danzi = 0
    for i in range(N):
        for j in range(N):
            house = dfs(i, j)
            if house != 0:
                housing.append(house)
                danzi += 1


sol()
PR()
