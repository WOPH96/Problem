def solution(n):
    answer = 0

    lst = []
    n = str(n)
    for num in n:
        lst.append(int(num))
    lst.sort()
    print(lst)

    while(lst):
        answer += lst.pop() * (10**len(lst))

    return int(answer)


print(solution(123412123))
