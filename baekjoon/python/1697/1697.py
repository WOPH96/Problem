from collections import deque
import sys
# sys.stdin = open('1697_input.txt', 'r')

n, k = map(int, input().split())

'''
bfs로 접근?
5 -> 27
3, 100000
중복 제거 

'''

visited = [0] * 100001


def bfs(start, end):
    visited[start] = 1
    q = deque()
    q.append(start)
    while q:
        v = q.popleft()
        # print(visited[:end+1])
        if v+1 < 100001 and visited[v+1] == 0:
            visited[v+1] = visited[v]+1
            q.append(v+1)
        if v-1 >= 0 and visited[v-1] == 0:
            visited[v-1] = visited[v]+1
            q.append(v-1)
        if 2*v < 100001 and visited[2*v] == 0:
            visited[2*v] = visited[v]+1
            q.append(2*v)
        if visited[end] != 0:
            break


bfs(n, k)
# print(visited[:k+1])
print(visited[k]-1)
