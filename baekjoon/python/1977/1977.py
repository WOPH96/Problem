import sys
sys.stdin = open('1977_input.txt','r')
M = int(input())
N = int(input())


# def check(x):
#     return int(x**(1/2))**2==x

'''
작은 자연수 제곱해서 큰값까지 가는게 낫겠는데
1<=M<=N<=10000 자연수니까
최대 10000 -> 100이 최대

idx=0으로 시작해서
범위에 걸릴떄까지 한칸씩 오른쪽 이동

범위 안걸리고 끝까지 가면 없는 것

범위 걸리면 처음 포인트 저장후 한칸씩 이동

최소포인트 ~ 최종포인트 제곱합
최소포인트 제곱값 출력 

'''
smalls = list(range(1,101))

point = 0
min_point=-1
while point<100:
    if M<=(smalls[point]**2)<=N:
        min_point=point
        point+=1
        break
    point+=1
if min_point == -1:
    print(min_point) 
    exit()

while point<100:
    if M<=(smalls[point]**2)<=N:
        point+=1
    else:
        break

print(sum(map(lambda x:x**2,smalls[min_point:point])))
print(smalls[min_point]**2)

