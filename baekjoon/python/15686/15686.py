import sys
sys.stdin = open('15686_input.txt', 'r')

n, m = map(int, input().split())

city = [list(map(int, input().split())) for _ in range(n)]

for elem in city:
    print(elem)

'''

'''
