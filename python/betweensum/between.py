def min_swap(a, b):
    if(a <= b):
        pass
    else:
        temp = a
        a = b
        b = temp


def solution(a, b):
    answer = 0
    if(a <= b):
        pass
    else:
        temp = a
        a = b
        b = temp
    for i in range(a, b+1):
        answer += i
    return answer


print(solution(4, -3))
