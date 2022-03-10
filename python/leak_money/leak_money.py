# def sum(pr, cnt):
#     if cnt == 1:
#         return pr

#     return pr*cnt + sum(pr, cnt-1)

def sum(pr, cnt):
    s = 0
    for i in range(1, cnt+1):
        s += pr*i
    return s


def solution(price, money, count):
    answer = 0
    SUM = sum(price, count)
    if money < SUM:
        answer = SUM-money
    return answer


print(solution(3, 20, 4))
