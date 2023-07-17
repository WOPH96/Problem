import sys
sys.stdin = open('2444_input.txt', 'r')

n = int(input())

for i in range(n):
    print(" "*(n-i-1), end="")
    print("*"*(2*i+1))
for i in range(n-2, -1, -1):
    print(" "*(n-i), end="")
    print("*"*(2*i+1))
