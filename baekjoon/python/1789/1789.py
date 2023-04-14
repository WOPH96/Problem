import sys
sys.stdin = open('1789_input.txt', 'r')

# 서로다른 N개의 합이 S / N을 최대한 크게
# 작은 값부터 차례대로

s = int(input())

for i in range(1, s+1):
    if s - i < 0:
        break
    s -= i
    print(s)
    result = i

print(result)
