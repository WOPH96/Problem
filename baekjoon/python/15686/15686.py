import sys
sys.stdin = open('15686_input.txt', 'r')

n, m = map(int, input().split())

city = [list(map(int, input().split())) for _ in range(n)]

for elem in city:
    print(elem)

'''
1. 치킨집좌표 구하기
2. 1의좌표 구하기
3. 없어질 치킨집 구하기
'''
