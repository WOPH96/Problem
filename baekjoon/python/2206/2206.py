import sys
sys.stdin = open('2206_input.txt', 'r')

n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input())))
# for elem in graph:
#     print(elem)

'''
벽을 부숴
최단거리니 bfs는 맞다

벽을 부순 케이스와 아닌 케이스로 나눠서 진행
'''

# 이동경로 그래프, 3차원으로 나누어 벽을 부순 경우를 저장하도록
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
# print(visited)
# 3번째 값이 벽부순case

from collections import deque
def bfs(G,v,status):
    q= deque()
    q.append((v,status))
    visited[v[0]][v[1]][status] = 1

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    while q:
        (x,y),status = q.popleft()
        # print(x,y,status)
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            #틀에 닿지 않은 경우에만 진행
            if 0<=nx<n and 0<=ny<m:
                # 방문한 적이 없으면서, 벽이 아닌 경우 
                if visited[nx][ny][status]==0 and G[nx][ny] == 0 :
                    visited[nx][ny][status] = visited[x][y][status] +1
                    q.append(((nx,ny),status))
                # 벽을 깬적이 없는 경우
                if status == 0 :
                    # 방문한 적이 없으면서, 벽이 있는 경우
                    if  visited[nx][ny][0]==0 and G[nx][ny] == 1:
                        visited[nx][ny][1]= visited[x][y][0]+1
                        q.append(((nx,ny),1))
                #벽이 아닌 경우 = 0
                
                #벽인 경우 else if가 아닌 그냥 if 로 진행해야하나 ?
        
    pass

bfs(graph,(0,0),0)

#두 케이스로 모두 진입 성공한 경우, 더 작은 거리 선택
a = visited[n-1][m-1][0] # 벽 안 깼을 때 목적지
b = visited[n-1][m-1][1] # 벽 깼을 때 목적지

if a!=0 and b!=0:
    print(min(a,b))
elif a==0 and b!=0:
    print(b)
elif a!=0 and b==0:
    print(a)
else:
    print(-1)
