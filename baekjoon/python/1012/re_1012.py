import sys
sys.setrecursionlimit(10 ** 6)
sys.stdin = open('1012_input.txt', 'r')

T = int(input())

for _ in range(T):
    m,n,k = map(int,input().split())
    # print(m,n,k)
    # graph = [[0]*m for _ in range(n)]
    graph = [[0 for _ in range(m)]for _ in range(n)]
    visited = [[False for _ in range(m)]for _ in range(n)]
    for _ in range(k):
        b,a = map(int,input().split())
        graph[a][b] = 1

    # for elem in graph:
    #     print(elem)
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    def dfs(i,j):
        #탈출
        if not (0<=i<n and 0<=j<m):
            return False
        if visited[i][j]:
            return False
        #구현
        #하나라도 찾으면 최종 출력 true
        if not visited[i][j] and graph[i][j]==1:
            visited[i][j] = True
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)
            return True
        pass
    cnt = 0
    for i in range(n):
        for j in range(m):
            if dfs(i,j):
                cnt+=1
    # for elem in visited:
    #     print(elem)
    print(cnt)