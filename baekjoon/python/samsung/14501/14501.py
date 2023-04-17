import sys
sys.stdin = open('14501_input.txt', 'r')
'''
거꾸로 가면서 최대이득 탐지 !
'''

n = int(input())
works = [list(map(int, input().split())) for _ in range(n)]
# print(works)
'''
내풀이, dp 
'''
money = [0]*n

for i in range(n-1, -1, - 1):
    present = works[i][0]
    future = i+present

    # 미래까지 일할수 있으면
    if future <= n:
        # 현재금액 저장
        money[i] += works[i][1]
        # 미래금액 중 최고가 저장x
        if future < n:
            MAX = 0
            for j in range(future, n):
                MAX = max(MAX, money[j])
            money[i] += MAX
    # print(money)
print(max(money))

'''
dfs남의풀이
'''
