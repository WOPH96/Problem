
def solution(arr):
    answer = []
    for member in arr:
        if not answer:
            answer.append(member)
        if member != answer[-1]:
            answer.append(member)
    return answer


print(solution([1, 1, 3, 3, 0, 1, 1]))
