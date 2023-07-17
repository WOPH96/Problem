import sys
sys.stdin = open('2480_input.txt', 'r')

a, b, c = map(int, input().split())

arr = [0]*7

for elem in [a, b, c]:
    arr[elem] += 1

M = max(arr)

if M == 3:
    print(10000+arr.index(3)*1000)
elif M == 2:
    print(1000+arr.index(2)*100)
else:
    print(max(a, b, c)*100)
