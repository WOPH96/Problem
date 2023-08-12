import sys
import heapq as hq
sys.stdin = open('1764_input.txt', 'r')
input = sys.stdin.readline
n, m = map(int, input().split())

common = []

# wolisten = [input().strip() for _ in range(n)]
# wosee = [input().strip() for _ in range(m)]
# # print(wolisten)

# for elem in wosee:
#     if elem in wolisten:
#         # common.append(elem)
#         hq.heappush(common,elem)

# print(len(common))
# while common:
#     print(hq.heappop(common))

names = dict()

for i in range(n+m):
    name = input().strip()
    if not names.get(name):
        names[name]=1
    else:
        hq.heappush(common,name)

print(len(common))
while common:
    print(hq.heappop(common))