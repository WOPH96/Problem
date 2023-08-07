import sys


def solution(targets):
    answer = 0
    targets.sort(lambda x: [x[1], x[0]])
    # print(targets)
    s = []
    s.append(targets.pop())
    while targets:
        start, end = targets.pop()
        if start >= s[-1][1]:
            s.append([start, end])
    print(len(s))
    return answer


solution([[4, 5], [4, 8], [10, 14], [11, 13], [5, 12], [3, 7], [1, 4]])
