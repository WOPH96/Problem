def solution(arr):
    answer = []
    if len(arr) == 1:
        answer.append(-1)
    else:
        #sorted(arr, reverse=1)
        # arr.pop()
        # answer.extend(arr)
    return answer


print(solution([4, 3, 2, 1]))
print(solution([10]))
