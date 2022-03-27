import heapq  # 리스트를 힙처럼 사용할 수 있게 해줌


def solution(priorities, location):
    answer = 0
    hb = []
    res = []
    for i in range(len(priorities)):
        # heapq.heappush(hb, priorities[i])
        heapq.heappush(hb, (-priorities[i], i))
    print(hb)

    while hb:
        x, y = heapq.heappop(hb)
        res.append((-x, y))
    print(res)
    return answer


print(solution([2, 1, 3, 2], 2))
# print(solution([1, 1, 9, 1, 1, 1], 0))
