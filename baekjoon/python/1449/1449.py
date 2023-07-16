import sys
sys.stdin = open('1449_input.txt','r')

n,l = map(int,input().split())

pos = list(map(int,input().split()))
pos.sort()
# print(pos)

'''
0.5~2.5 = 2 
l-1 커버되면 ok
stack에 넣고 맨위엣놈이 커버 못하면 추가로 넣어

'''

stack = []
stack.append(pos[0])

for i in range(1,n):
    if pos[i] - stack[-1] <= l-1  : # 현재 위치 - 마지막 위치 <= 테이프-1 : 커버 가능
        pass
    else : #커버 불가능
        stack.append(pos[i])

# print(stack)
print(len(stack))