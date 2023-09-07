import sys
sys.stdin = open('1952_input.txt','r')
input = sys.stdin.readline

n,m = map(int,input().split())

if n==2 and m==2:
    print(2)
    exit()

visited= [[0 for _ in range(m)]for _ in range(n)]

# print(visited)

dx=[0,1,0,-1]
dy=[1,0,-1,0]

cnt = 0
i=0

x=y=0
visited[x][y]=1

from collections import  deque

q = deque()
q.append((0,0))

while q:
    x,y = q.popleft()
    i%=4
    nx,ny = x+dx[i],y+dy[i]
    
    if 0<=nx<n and 0<=ny<m:
        if not visited[nx][ny]:
            visited[nx][ny]=1
            q.append((nx,ny))
        else:
            ti = (i+1)%4
            tx,ty = x+dx[ti],y+dy[ti]
            if visited[tx][ty]:
                break
            else:
                cnt+=1
                i+=1
                q.append((x,y))
                
    else:
        cnt+=1
        i+=1
        q.append((x,y))

    for elem in visited:
        print(elem)
    print(cnt)
    # break
