import sys
sys.stdin = open('1075_input.txt','r')

N = int(input())
F = int(input())

# print(N,F)
'''
N = N-N%100 = 맨뒤가 00인것 구하기
int(N/F) 구하기
이 값에서부터 계속 증가 나누어떨어지면 끝
'''

N= N-N%100
target = int(N/F)*F
# print(N,target)

while True:
    if N<=target<N+100:
        break
    target+=F
target%=100
if target<10:
    print('0'+str(target))
else:
    print(target)