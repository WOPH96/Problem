import sys
sys.stdin = open('1012_input.txt', 'r')

T = int(input())

for _ in range(T):
    m,n,k = map(int,input().split())
    print(m,n,k)
    # graph = [[0]*m for _ in range(n)]
    graph = [[0 for _ in range(m)]for _ in range(n)]
    
    for _ in range(k):
        b,a = map(int,input().split())
        graph[a][b] = 1

    for elem in graph:
        print(elem)

    def dfs():
        pass
    cnt = 0
    for i in range(n):
        for j in range(m):
            if dfs(i,j):
                cnt+=1