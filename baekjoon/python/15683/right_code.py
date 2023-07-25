import sys
sys.stdin = open('15683_input.txt','r')

import copy
n, m = map(int, input().split())
cctv = []
graph = []
mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]],
]

# 북 - 동 - 남 - 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    data = list(map(int, input().split()))
    graph.append(data)
    for j in range(m):
        if data[j] in [1, 2, 3, 4, 5]:
            cctv.append([data[j], i, j])
# for elem in cctv:
#     print(elem)
#이해 완료, 
# graph를 받아서 
def fill(board, mm, x, y):
    for i in mm:
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                break
            if board[nx][ny] == 6:
                break
            elif board[nx][ny] == 0:
                board[nx][ny] = 7

def dfs(depth, arr):
    global min_value

    if depth == len(cctv): # 모든 cctv 돌았다면
        count = 0 # 사각지대 카운트 시작
        for i in range(n):
            count += arr[i].count(0)
        min_value = min(min_value, count) 
        return #종료 -> temp = copy.deepcopy(arr)로 이동
    temp = copy.deepcopy(arr) # 기존 그래프가 변하지 않도록 설정
    cctv_num, x, y = cctv[depth] # n번째 cctv 종류와 위치 
    for i in mode[cctv_num]: # 해당 타입 cctv의 모든 방향 
        fill(temp, i, x, y) # 빛으로 쬐기
        dfs(depth+1, temp) # n+1번째 cctv로 진행
        temp = copy.deepcopy(arr) # 1번 라인 돌았으니 초기 그래프로 다시 설정


min_value = int(1e9)
dfs(0, graph)
print(min_value)