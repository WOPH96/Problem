import sys
sys.stdin = open('2644_input.txt','r')

n = int(input())
ps1,ps2 = map(int,input().split())
relation = int(input())

children = [[]for _ in range(n+1)]
parent = [0] * (n+1)
visited= [False]*(n+1)

for i in range(relation):
    p,c = map(int,input().split())
    children[p].append(c)
    parent[c]=(p)

from collections import deque

def bfs(p1,p2):
    q = deque()
    chon=0
    cur=p1
    while True:
        q.append((cur,chon))
        #자식노드 탐방
        while q:
            out,cchon = q.popleft()
            if not visited[out]:
                visited[out]=True
                if out==p2:
                    return cchon
                for child in children[out]:
                    if child==p2:
                        return cchon+1
                    else:
                        q.append((child,cchon+1))

        #자식중에 못찾았으면 부모노드 탐방
        if not parent[cur]:
            return -1
        else:
            cur = parent[cur]
            chon+=1

            
    pass

print(bfs(ps1,ps2))

# print(children)
# print(parent)