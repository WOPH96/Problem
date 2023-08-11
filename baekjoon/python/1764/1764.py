import sys
sys.stdin = open('1764_input.txt', 'r')
n, m = map(int, input().split())

common = []

wolisten = [sys.stdin.readline() for _ in range(n)]

print(wolisten)

for _ in range(m):
    wosee = sys.stdin.readline()
    if wosee in wolisten:
        common.append(wosee)

common.sort()
print(len(common))
for elem in common:
    print(elem)
