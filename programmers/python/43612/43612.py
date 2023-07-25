import sys
sys.stdin = open('43612_input.txt','r')

def solution(n, computers):
    answer = 0
    # print(n,computers)

    from collections import deque
    visited=[False]*n
    def bfs(G,v):
        q = deque()
        q.append(v)
        while q:
            out = q.popleft()
            if not visited[out] :
                
                visited[out] = True
                for nv,connect in enumerate(G[out]):
                    if nv != out and connect==1:
                        # print(out,nv,connect)
                        q.append(nv)
    
    for i in range(n):
        if not visited[i]:
            bfs(computers,i)
            # print()
            answer+=1

    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))