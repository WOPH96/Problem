import sys
sys.setrecursionlimit(10**5)
# sys.stdin = open('2468_input.txt', 'r')
'''
안전 영역
초기 높이-1 부터 끝까지 물채워버리기

개수 카운트,

graph - rain만큼 빼서
saved = 1
safe = 0


'''
n = int(input())
cnts = [0]*n

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 잠기는 녀석들 집합
saved = [[0 for _ in range(n)]for _ in range(n)]
max_high = max(map(max, graph))
cnts = [0]*(max_high+1)


def prmat(gr):
    for row in gr:
        print(row)
    print()

# 계산 초기화


def init_saved():
    global saved
    saved = [[0 for _ in range(n)]for _ in range(n)]


def dfs(x, y, rain):
    # 벽 넘었는가 ? = 찾는 곳 아님
    if not (0 <= x < n and 0 <= y < n):
        return False
    # 잠겼는가? = 찾는 곳 아님
    if graph[x][y] <= rain:
        # flooded 할필요 없을듯? 그냥 이렇게만 비교
        return False
    # 이미 찾은 안전구역인가 ? True로 해도 별 상관 없을듯, 어짜피 거르는게 목적
    if saved[x][y] == 1:
        return False
    # 벽도 아니고 잠기지도 않았다면 안전구역
    # 주변 안전구역 다 찾기
    saved[x][y] = 1
    dfs(x, y-1, rain)
    dfs(x, y+1, rain)
    dfs(x-1, y, rain)
    dfs(x+1, y, rain)
    return True


for rain in range(0, max_high+1):
    for i in range(n):
        for j in range(n):
            if dfs(i, j, rain) == True:
                cnts[rain] += 1
    init_saved()
    # print(graph)
    # prmat(saved)
# print(cnts)
print(max(cnts))
