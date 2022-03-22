'''
100 2
90 1
70 2
'''


import sys

safe=[]
result = 0
M,N = map(int,sys.stdin.readline().split())
for _ in range(N): #종류만큼
    safe.append(list(map(int,sys.stdin.readline().split())))

safe.sort(key=lambda x:x[1])
#print(safe)

while safe:
    weight, money = safe.pop()
    if M>=weight:
        M-=weight
        result += money*weight
    else:
        result += money*M
        break

print(result)