import sys
sys.stdin = open('1065_input.txt', 'r')
# 첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.

n = int(input())

'''
100부터 ㄱㄱ
1~99는 전부 ok
1 0 0 X
첫째 자리 - 둘쨰자리 저장
둘쨰 - 셋째 = 저장값이랑 동일하면 ok
'''

cnt = 0


def check(num):  # 등차수열 체크 맞으면 1 아니면 0  // 3자리만 체크 ~
    h = t = o = 0
    h = int(num/100)
    num %= 100
    t = int(num/10)
    num %= 10
    o = num
    val = h-t
    if (t-o) == val:
        return 1
    else:
        return 0


if n < 100:
    cnt = n
else:
    cnt = 99
    for i in range(100, n+1):
        cnt += check(i)
print(cnt)
