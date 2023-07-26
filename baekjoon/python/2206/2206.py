import sys
sys.stdin = open('2206_input.txt', 'r')

n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input())))

print(graph)
