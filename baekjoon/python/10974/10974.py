import sys
sys.stdin = open('10974_input.txt','r')

n = int(input())

from itertools import permutations

for elem in permutations(range(1,n+1)):
    for num in elem:
        print(num,end=" ")
    print()