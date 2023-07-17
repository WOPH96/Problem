import sys
sys.stdin = open('3003_input.txt', 'r')

Input = list(map(int, input().split()))
# print(Input)
Right = [1, 1, 2, 2, 2, 8]

answer = list(map(lambda a, b: a-b, Right, Input))
for i in answer:
    print(i, end=" ")
