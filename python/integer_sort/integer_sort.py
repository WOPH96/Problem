def solution(n):

    n = list(str(n))
    answer = "".join(sorted(n, reverse=True))

    return int(answer)


print(solution(90009))
