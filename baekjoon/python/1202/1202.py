import sys
import heapq as hq
sys.stdin = open('1202_input.txt','r')

n,k = map(int,sys.stdin.readline().split())

#보석 m,v 
jws = []

for _ in range(n):
    weight,value = map(int,sys.stdin.readline().split())
    jws.append([weight,value])

bags = []
for _ in range(k):
    c = int(sys.stdin.readline())
    bags.append(c)

# print(jws,bags,visited,sep="\n")
jws.sort()
bags.sort() # 작은 가방 순서로 정렬

    
# print(jws,bags,sep="\n")
'''
모든 가방을 돌면서 해당 무게보다 가벼운 보석들 넣기
가방보다 무거운 보석 나왔을 때 멈추고
그중에 가장 비싼 보석 저장

다음 보석부터 다시 돌아

'''
sum=0
idx=0
heap = []
for bag in bags:
    while(idx<n and bag>=jws[idx][0]):
        hq.heappush(heap,[-jws[idx][1],jws[idx][1]])
        idx+=1
    if(heap):
        sum+=hq.heappop(heap)[1]    

print(sum)        


    

'''

제일 비싼 가격을 받아야 하니까
가격순 정렬
11,100  = 못먹는거
3,99    = 젤작은걸론 못먹
10,65   = 먹을 수 있음
2,23    = 먹을수 있음 


못담아가면 버리는거지
그럼 제일 비싼거 뽑아서
작은 가방이 담을수있어야


작은 가방이 먹을 수 있는 거 위에서부터 고르기
2 -> 2,99
10 -> 1,65
99+65 = 164



''' 