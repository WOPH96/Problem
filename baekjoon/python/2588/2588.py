import sys
sys.stdin = open('2588_input.txt', 'r')

lst = [input() for _ in range(2)]
mul = []
res = 0

target = int(lst[0])
for i, num in enumerate(reversed(lst[1])):
    val = target * int(num)
    mul.append(val)
    print(val)
# print(mul)
for i, num in enumerate(mul):
    res += 10**i * num

print(res)
