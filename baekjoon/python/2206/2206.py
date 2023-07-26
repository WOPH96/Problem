import sys
sys.stdin = open('2206_input.txt', 'r')

n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input())))

print(graph)

'''
벽을 부숴
최단거리니 bfs는 맞다

이동하는 중에 마주치는 벽을 부숴야함

'''
