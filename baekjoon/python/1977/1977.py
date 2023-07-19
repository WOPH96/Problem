import sys
sys.stdin = open('1977_input.txt','r')
m = int(input())
n = int(input())

print(m,n)

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
print(smalls)

