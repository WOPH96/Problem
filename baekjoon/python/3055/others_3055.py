import sys
sys.stdin = open('3055_input.txt','r')

n, m = map(int,input().split())

Ggraph=[]
GSvisited=[[0]*m for _ in range(n)] # 고슴도치 방문 확인
GWvisited=[[0]*m for _ in range(n)] # 물 방문 확인
pos_S = []
pos_W = []


for i in range(n):
    tmp = list(input())
    if 'S' in tmp:
        pos_S.append([i,tmp.index('S')])
        GSvisited[i][tmp.index('S')] = 1
    if '*' in tmp:
        Ws =[[i,j] for j,x in enumerate(tmp) if x in "*"]
        for x,y in Ws:
            GWvisited[x][y] = 1
        pos_W.extend(Ws)
    Ggraph.append(tmp)

def printGraphes(comment=None,Lgraph=Ggraph,LSvisited=GSvisited,LWvisited=GWvisited):
    if comment:
        print(comment)
    tap="\t"*(int(m//2.5))
    print("Graph ",end=tap*2)
    print("GVisited ",end=tap)
    print("Wvisited ")
    for elem1, elem2, elem3 in zip(Lgraph,LSvisited,LWvisited):
        print(elem1, end="\t")
        # elem2=list(map(lambda x:"{:^1}".format(x),elem2))
        print(elem2, end='\t')
        # elem3=list(map(lambda x:"{:^1}".format(x),elem3))
        print(elem3)
    print()

# printGraphes()

'''
물은 알아서 퍼지도록 냅둔다 -> 대신 퍼지는 순서를 저장
고슴도치가 이동할때, 물이 퍼지는 타이밍엔 거길로 이동하지 못한다고 설정

'''

# print(pos_S,pos_W)

from collections import deque

def bfs():
    wq = deque(pos_W)
    sq = deque(pos_S)
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    #물 먼저
    while wq:
        x,y = wq.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if Ggraph[nx][ny] =='.' or Ggraph[nx][ny]=='S':
                    if not GWvisited[nx][ny]:
                        GWvisited[nx][ny]=GWvisited[x][y]+1
                        wq.append((nx,ny))
    
    while sq:
        x,y = sq.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if Ggraph[nx][ny] == 'D':
                    return GSvisited[x][y]
                if Ggraph[nx][ny] == '.' and (GSvisited[x][y]+1< GWvisited[nx][ny] or GWvisited[nx][ny]==0):
                    if not GSvisited[nx][ny]:
                        GSvisited[nx][ny]=GSvisited[x][y]+1
                        sq.append((nx,ny))

                    
    return "KAKTUS"
# print(pos_S)
print(bfs())
# printGraphes()
