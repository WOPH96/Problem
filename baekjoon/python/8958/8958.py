import sys
sys.stdin = open('8958_input.txt','r')

t = int(input())

for _ in range(t):
    OXs = list(input())
    # print(OXs)
    sum = 0
    cont = 1
    for OX in OXs:
        if OX=='O':
            sum+=cont
            cont+=1
        else:
            cont=1
    print(sum)