# import sys
# sys.stdin = open('4673_input.txt','r')

# 10,000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 증가하는 순서로 출력한다.
'''
셀프넘버
1부터 dp 조지기?
recursive로 채워
1+1 = 2
2+2 = 4
3+3 = 6
4+4 = 8
5+5 = 10
6+6 = 12
..
10+1+0=11

1 -> 1+1 -> 2 -> 2+2 -> 4 -> 4+4 -> 8 -> 8+8 -> 16 -> 16+1+6 -> 23 -> 23+2+3 -> 28

'''

dp = [0]*10001


def posnum(num):

    sum = 0
    for i in range(4, -1, -1):
        sum += int(num/(10**i))
        num %= 10**i
    return sum


def recursive(num):  # dp가 0이라면 계속 진행 / 10000보다 작다면 계속 진행
    num += posnum(num)
    if num > 10000:  # 10000으로 수정
        return 0
    if dp[num] == 0:
        dp[num] = 1
        return recursive(num)
    else:
        return 0


for i in range(10001):
    recursive(i)

for i, num in enumerate(dp):
    if num == 0:
        print(i)
