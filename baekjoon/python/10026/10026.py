import sys
sys.setrecursionlimit(10**5)
# sys.stdin = open('10026_input.txt', 'r')

'''
R=G / B
R / G / B
두개로 나눠서
구역! 해당구간 아니면 ㄱㄱ
dfs
'''

n = int(input())

graph = [input() for _ in range(n)]

can_visit = [[0 for _ in range(n)] for _ in range(n)]
cant_visit = [[0 for _ in range(n)] for _ in range(n)]

# 구별가능할때


def sep(gr):
    for elem in gr:
        print(elem)
    print()


def dfs_can(x, y, color):

    # 벽 벗어났으면
    if not (0 <= x < n and 0 <= y < n):
        return False
    # 방문했던곳이면
    if can_visit[x][y] == 1:
        return False
    # 해당 컬러랑 다른곳이면
    if color != graph[x][y]:
        return False
    # 해당 컬러랑 같은 곳이고, 방문했던 곳 아니면 전부 채워
    can_visit[x][y] = 1
    # sep(can_visit)
    dfs_can(x, y-1, color)
    dfs_can(x, y+1, color)
    dfs_can(x-1, y, color)
    dfs_can(x+1, y, color)
    return True


def dfs_cant(x, y, color):
    # 벽 벗어났으면
    if not (0 <= x < n and 0 <= y < n):
        return False
    # 방문했던곳이면
    if cant_visit[x][y] == 1:
        return False
    # 해당 컬러랑 다른곳이면
    if color != graph[x][y]:
        if (color == 'G' and graph[x][y] == 'R') or (color == 'R' and graph[x][y] == 'G'):
            pass
        else:
            return False
    # 해당 컬러랑 같은 곳이고, 방문했던 곳 아니면 전부 채워
    cant_visit[x][y] = 1
    # sep(cant_visit)
    dfs_cant(x, y-1, color)
    dfs_cant(x, y+1, color)
    dfs_cant(x-1, y, color)
    dfs_cant(x+1, y, color)
    return True


cnts = [0]*2

for i in range(n):
    for j in range(n):
        if dfs_can(i, j, graph[i][j]) == True:
            cnts[0] += 1
            # print("========")
        if dfs_cant(i, j, graph[i][j]) == True:
            cnts[1] += 1
            # print("========")
for cnt in cnts:
    print(cnt, end=" ")
