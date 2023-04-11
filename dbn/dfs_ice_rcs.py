import sys

sys.stdin = open("ice_input.txt","r")

n, m = map(int,input().split())

graph = [ list(map(int,input())) for _ in range(n) ]

# print(graph)

def dfs(x,y):

    #벽이면
    if x <0 or x>=n or y <0 or y>=m:
        return False
    #막혔으면
    if graph[x][y] == 1:
        return False

    #구멍이면
    elif graph[x][y]== 0 :
        #주변 찾아서 다 바꿔줘야함
        graph[x][y]=1
        dfs(x,y-1)
        dfs(x,y+1)
        dfs(x-1,y)
        dfs(x+1,y)

        return True


def sol():
    ice=0
    for i in range(n):
        for j in range(m):
            if dfs(i,j)==True:
                ice+=1
    print(ice)
sol()