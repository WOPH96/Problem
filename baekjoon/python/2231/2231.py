import sys
sys.stdin = open('2231_input.txt', 'r')

n = int(input())


def pos_sum(num):
    sum = 0
    for i in range(6, -1, -1):
        sum += int(num/(10**i))
        num %= 10**i
    return sum


find_flag = False
for i in range(n):
    if i+pos_sum(i) == n:
        find_flag = True
        break
print(i if find_flag == True else 0)
