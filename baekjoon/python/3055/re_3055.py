import sys
sys.stdin = open('3055_input.txt','r')

n, m = map(int,input().split())

Ggraph=[]
Gvisited=[[False]*m for _ in range(n)]
pos_S = []
pos_W = []

for i in range(n):
    tmp = list(input())
    if 'S' in tmp:
        pos_S.extend([i,tmp.index('S')])
        # Gvisited[i][tmp.index('S')] = True
    if '*' in tmp:
        Ws =[[i,j] for j,x in enumerate(tmp) if x in "*"]
        pos_W.extend(Ws)
    Ggraph.append(tmp)

def printGraphes(comment=None,Lgraph=Ggraph,Lvisited=Gvisited):
    if comment:
        print(comment)
    print("Graph ",end="\t\t\t")
    print("Visited ")
    for elem1, elem2 in zip(Lgraph,Lvisited):
        print(elem1, end="\t")
        elem2=list(map(lambda x:"{:^1}".format(x),elem2))
        print(elem2)
    print()

from collections import deque
from copy import deepcopy

dx=[1,-1,0,0]
dy=[0,0,1,-1]

#홍수 범람, 한 턴만 진행
#마지막 홍수 지점들 리턴
def flood(Lgraph,q:deque)->deque:
    rq = deque()
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if Lgraph[nx][ny]=='.':
                    Lgraph[nx][ny]='*'
                    rq.append((nx,ny))
    return rq

# 고슴도치는 물 일어날 예정인 곳으론 이동할 수 없으므로, 
# 홍수가 먼저 일어난다고 설정
# printGraphes("처음")
# 첫 홍수



# 움직임 시작 
# 이전 방식으로 할 것인지, 아니면 for문 새로 만들지 고민

'''
flood한번, move 한번
가장 처음은 flood 이후 진행 

S는 not visited & . 인 곳으로만 이동할수 있음
한번 이동하는 것은 전부 다른 케이스

(3,0) -> (4,0), (2,0) 으로 이동 가능
이동 하면, Graph / visited 변경되어야함
홍수 발생 -> queue 리턴
queue 값도 각각 저장되어야 함 -> graph 다르면 어짜피 그렇게 됨

'''

Gm = 10**6
def move(x,y,graph,visited,flood_pos,cnt):
    global Gm
    global n
    global m
    # print(x,y)

    #탈출 조건
    ## 찾았으면
    if not (0<=x<n and 0<=y<m):
        return 
    
    #여러 경로중에서 최솟값 저장
    if graph[x][y] == 'D':
        Gm = min(Gm,cnt)
        return

    # 틀 벗어났거나, 방문했던 장소라면 끝 
    if visited[x][y] or graph[x][y]=='X' or graph[x][y]=='*':
        return

    #구현
    ##이동
    ##각각의 그래프, 방문 생성
    Lgraph = deepcopy(graph)
    Lvisited = deepcopy(visited)
    Lflood = deepcopy(flood_pos)
    Lvisited[x][y] = True

    if Lgraph[x][y] == '.':
        Lgraph[x][y]='S'

    Lflood = flood(Lgraph,Lflood)
    
    # printGraphes(f"{x,y} 홍수 후",Lgraph=Lgraph,Lvisited=Lvisited)
    Lgraph[x][y] = '.'
    
    
    move(x+1,y,Lgraph,Lvisited,Lflood,cnt+1)
    move(x-1,y,Lgraph,Lvisited,Lflood,cnt+1)
    move(x,y-1,Lgraph,Lvisited,Lflood,cnt+1)
    move(x,y+1,Lgraph,Lvisited,Lflood,cnt+1)



#초기 graph,visited,홍수 시작점 좌표 전달
move(pos_S[0],pos_S[1],Ggraph,Gvisited,deque(pos_W),0)

print("KAKTUS" if Gm ==1000000 else Gm)
