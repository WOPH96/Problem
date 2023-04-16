import sys
sys.stdin = open('10162_input.txt', 'r')

T = int(input())

buttons = [300, 60, 10]
cnt = [0]*3

# T ,300 -> 100//300 = 0 100%300 = 100
# T ,60  -> 100//60 =  1 100%60 = 40

for i in range(3):
    cnt[i] = T//buttons[i]
    T %= buttons[i]

if T != 0:
    print(-1)
else:
    for i in cnt:
        print(i, end=" ")
