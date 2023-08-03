import sys
sys.stdin = open('16234_input.txt','r')

n,l,r = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(n)]

for elem in graph:
    print(elem)

'''

모든 구간 돌면서 연합국 만들 수 있는 지 체크 + 합산
visited이면 안해도 됨
다 돌고나서야 합 구할 수 있음


'''
from collections import deque
from copy import deepcopy

zeros = [[0]*n for _ in range(n)]

#이사 성공하면 true, 실패하면 false 리턴
def bfs ()->bool:
    union = deepcopy(zeros)
    q = deque()
    q.append()
    pass

cnt=0
while bfs():
    cnt+=1
