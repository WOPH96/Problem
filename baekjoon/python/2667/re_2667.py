import sys
sys.setrecursionlimit(10 ** 6)
sys.stdin = open('2667_input.txt', 'r')

n= int(input())

graph = []
visited = [[False for _ in range(n)]for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int,input())))

for elem in graph:
    print(elem)
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def dfs(i,j,cnt):
    #탈출
    if not (0<=i<n and 0<=j<n):
        return False
    if visited[i][j]:
        return False
    #구현
    #하나라도 찾으면 최종 출력 true
    if not visited[i][j] and graph[i][j]==1:
        visited[i][j] = True
        cnt+=1
        print(cnt)
        dfs(i-1,j,cnt)
        dfs(i+1,j,cnt)
        dfs(i,j-1,cnt)
        dfs(i,j+1,cnt)
        return True
    pass
cnt = 0
res = []
for i in range(n):
    for j in range(n):
        if dfs(i,j,cnt):
            res.append(cnt)
            cnt=0
for elem in visited:
    print(elem)
print(res)