# def solution(n):
#     i = 0
#     prime = 0
#     for num in range(2, n+1):
#         for q in range(2, num+1):
#             if num % q == 0:
#                 i += 1
#         if i == 1:
#             prime += 1
#         i = 0
#     return prime

# 소수 = 이전의 소수로 안나눠떨어지면 소수?

def solution(n):
    prime = [2]

    for i in range(2, n+1):
        for num in prime:
            if i % num != 0:
                break
        if num == prime[-1]:
            prime.append(i)
            print(prime)

    return len(prime)


print(solution(10))
# print(solution(5))
# print(solution(1000000))
