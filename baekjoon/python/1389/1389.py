import sys
sys.stdin = open('1389_input.txt', 'r')

n, m = map(int, input().split())

graph = [[]for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

'''
heapq (케빈베이컨 수, 번호)로 저장
오름차순으로 정렬되니 맨앞에 있는애가 된다

visited 매 노드마다 초기화
bfs 돌면서, 한 다리 건널때마다 방문횟수 1증가
도착했을때 visited 0이면 방문횟수 저장
모든 노드 돌았을때 visited 총합 = kebin vacon

'''
import heapq as hq
from copy import deepcopy
from collections import deque
# a = []
# hq.heappush(a,(6,3))
# hq.heappush(a,(3,1))
# hq.heappush(a,(3,2))
# print(a[0])

kebin = []
visited = [-1]*(n+1)

#노드 받아서 kebin 값 전달
def bfs(node)->int:
    node_visited = deepcopy(visited)
    q = deque()
    q.append((node,0))
    while q:
        v,dist = q.popleft()
        # print(v,dist,node_visited)
        if node_visited[v]== -1:
            node_visited[v] = dist
            for nv in graph[v]:
                q.append((nv,dist+1))
    # print(node_visited)
    return sum(node_visited)
for i in range(1,n+1):
    hq.heappush(kebin,(bfs(i)+1,i))

print(kebin[0][1])    

