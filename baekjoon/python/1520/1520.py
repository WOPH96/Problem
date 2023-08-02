import sys
sys.stdin = open('1520_input.txt','r')

n,m = map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]

# for elem in graph:
#     print(elem)

'''
dfs로 모든 경로 확인
'''

def dfs(init):
    s = []
    s.append(init)
    path=0
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    while s:
        x,y = s.pop()
        # print(x,y)
        if x==n-1 and y==m-1:
            path+=1
            continue
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny]<graph[x][y]:
                    s.append((nx,ny))
        
    return path

print(dfs((0,0)))
