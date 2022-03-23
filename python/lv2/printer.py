import heapq


def solution(priorities, location):
    answer = 0
    hb = []

    for i in range(len(priorities)):
        heapq.heappush(hb, priorities[i])

    while hb:
        print(heapq.heappop(hb))

    return answer


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
