import sys
sys.stdin = open('14916_input.txt','r')

n = int(input())

'''
5원 2원 .. 배수 관계가 아니니 애매하네

3가지 경우로 나눌 수 있을듯
1. 5의 배수인 경우
    5로 전부 한다
2
    가장 근접한 낮은 5의 배수로 나눈다 -> 나머지 2로 처리
3. 
    두번째로 근접한 낮은 5의 배수로 나눈다 -> 나머지 2로 처리
99 = 95+4
98 = 95+3 = 90+8
93 = 90+3 = 85+8
'''
def checkodd(val):
    return val%2
if n==1 or n==3:
    print(-1)
elif n%5==0:
    print(int(n/5))
else:
    costs=0
    if checkodd(n%5):
        costs+=int(n/5)-1
        n%=5
        n+=5
        costs+=int(n/2)
    else :
        costs+=int(n/5)
        n%=5
        costs+=int(n/2)
    print(costs)