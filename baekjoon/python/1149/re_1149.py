from itertools import product
from itertools import repeat
import sys
sys.stdin = open('1149_input.txt', 'r')

'''
문제
RGB거리에는 집이 N개 있다. 거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집이 순서대로 있다.

집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다. 각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.

1번 집의 색은 2번 집의 색과 같지 않아야 한다.
N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.
입력
첫째 줄에 집의 수 N(2 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 각 집을 빨강, 초록, 파랑으로 칠하는 비용이 1번 집부터 한 줄에 하나씩 주어진다. 집을 칠하는 비용은 1,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 모든 집을 칠하는 비용의 최솟값을 출력한다.
'''

n = int(input())

costs = [list(map(int, input().split())) for _ in range(n)]

# for elem in costs:
#     print(elem)

dp = [[0]*3 for _ in range(n)]

for i in range(3):
    dp[0][i] = costs[0][i]

for i in range(1, n):
    for j in range(3):
        m = 10**9
        for k in range(3):
            if k == j:
                continue
            else:
                m = min(m, dp[i-1][k])
        dp[i][j] += costs[i][j]+m
print(min(dp[n-1]))