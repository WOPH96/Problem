from math import *


def solution(n):
    answer = 0

    lst = []
    n = str(n)
    for num in n:
        lst.append(int(num))
    lst.sort()

    while(lst):
        answer += lst.pop()*pow(10, len(lst))

    return int(answer)


print(solution(118372))
