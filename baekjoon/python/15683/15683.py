import sys
sys.stdin = open('15683_input.txt','r')

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

for elem in graph:
    print(elem)

'''
idea :
1 -> 4가지 (상하좌우)
2 -> 2가지 (양방향)
3 -> 4가지 (ㄱ모양 4가지)
4 -> 4가지 (ㅓ모양 4가지)
5 -> 1가지 
'''
