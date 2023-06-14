import sys
sys.stdin = open('1202_input.txt','r')

n,k = map(int,sys.stdin.readline().split())

#보석 m,v 
jws = []
visited = [False]*n
for _ in range(n):
    m,v = map(int,sys.stdin.readline().split())
    jws.append([m,v])

bags = []
for _ in range(k):
    c = int(sys.stdin.readline())
    bags.append(c)

# print(jws,bags,visited,sep="\n")

jws.sort(key=lambda x:-x[1])
bags.sort()
# print(jws,bags,sep="\n")

sum = 0 
for bag in bags:
    for i in range(n):
        if bag >= jws[i][0] and not visited[i] :
            sum +=jws[i][1]
            visited[i] = True
            break
print(sum)

'''

제일 비싼 가격을 받아야 하니까
가격순 정렬
2,99
1,65
5,23

작은 가방이 먹을 수 있는 거 위에서부터 고르기
2 -> 2,99
10 -> 1,65
99+65 = 164

''' 