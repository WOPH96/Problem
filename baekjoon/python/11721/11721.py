import sys
sys.stdin = open('11721_input.txt', 'r')

string = input()

cnt = 0
for char in string:
    print(char, end="")
    cnt += 1
    if cnt % 10 == 0:
        print()
print()
