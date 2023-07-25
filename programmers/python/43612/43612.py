import sys
sys.stdin = open('43612_input.txt','r')

def solution(n, computers):
    answer = 0
    print(n,computers)

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
                    # print(G[out])
                    if nv == out:
                        continue
                    else:
                        if connect == 1:
                            q.append(nv)
                            visited[nv] = True

    for i in range(n):
        if not visited[i]:
            bfs(computers,i)
            answer+=1

    return answer


print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))