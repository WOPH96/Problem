import sys
from collections import deque

sys.stdin = open("ice_input.txt","r")

n, m = map(int,input().split())

graph = [ list(map(int,input())) for _ in range(n) ]

# print(graph)

def bfs(x,y):
    if graph[x][y] == 1:
        return False
    #이미 찾은 상태, 이제 주변 구멍을 메꿔야 함
    q = deque()
    q.append((x,y))
    #움직일 수 있는 범위
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while (q) :
        # 현위치
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #벽이면
            if nx <0 or nx>=n or ny <0 or ny>=m:
                continue
            #막혔으면
            if graph[nx][ny] == 1:
                continue
            #구멍이면, 주변 다 메꾸기
            elif graph[nx][ny]== 0 :
                q.append((nx,ny))
                graph[nx][ny] = 1
    return True


def sol():
    ice=0
    for i in range(n):
        for j in range(m):
            if bfs(i,j)==True:
                ice+=1
    print(ice)
sol()