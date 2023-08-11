import sys
sys.stdin = open('2675_input.txt', 'r')

t = int(input())
for _ in range(t):
    n, string = input().split()
    n = int(n)

    for elem in string:
        print(elem*n, end="")
    print()
