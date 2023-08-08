import sys


def solution(targets):
    answer = 0
    targets.sort(key=lambda x: [x[1], x[0]])
    # print(targets)

    p = 0
    for target in targets:
        if p <= target[0]:
            answer += 1
            p = target[1]

    print(answer)
    return answer


solution([[4, 5], [4, 8], [10, 14], [11, 13], [5, 12], [3, 7], [1, 4]])
