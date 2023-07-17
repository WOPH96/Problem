import sys
sys.stdin = open('2309_input.txt','r')

heights = [int(input()) for i in range(9)]
# print(heights)

'''
다 더한다음에 100을 뺴서 남는 애들 계산하면 되지 않을까
'''
key = sum(heights)-100
heights.sort()
breaker=False
# print(key)
for i in range(9):
    for j in range(i+1,9):
        if heights[i]+heights[j]==key:
            breaker=True
            break
    if breaker:
        break
for idx,elem in enumerate(heights):
    if idx not in (i,j):
        print(elem)
