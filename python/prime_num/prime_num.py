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
'''
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.3MB)
테스트 2 〉	통과 (0.56ms, 10.2MB)
테스트 3 〉	통과 (3.91ms, 10.1MB)
테스트 4 〉	통과 (17.85ms, 10.3MB)
테스트 5 〉	통과 (7.63ms, 10.2MB)
테스트 6 〉	통과 (1630.72ms, 10.1MB)
테스트 7 〉	통과 (126.44ms, 10.1MB)
테스트 8 〉	통과 (830.79ms, 10.1MB)
테스트 9 〉	통과 (2300.80ms, 10.1MB)
테스트 10 〉	실패 (시간 초과)
테스트 11 〉	실패 (시간 초과)
테스트 12 〉	실패 (시간 초과)
효율성  테스트
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	실패 (시간 초과)
'''


# def solution(n):
#     prime = [2]
#     if n == 2:
#         return 1
#     for i in range(3, n+1):
#         for num in prime:
#             if i % num == 0:
#                 break
#         if num == prime[-1]:
#             prime.append(i)

#     return len(prime)  # len(prime)


'''
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.08ms, 10.1MB)
테스트 3 〉	통과 (0.19ms, 10.2MB)
테스트 4 〉	통과 (0.58ms, 10.3MB)
테스트 5 〉	통과 (0.54ms, 10.2MB)
테스트 6 〉	통과 (48.14ms, 10.3MB)
테스트 7 〉	통과 (2.73ms, 10.3MB)
테스트 8 〉	통과 (19.83ms, 10.2MB)
테스트 9 〉	통과 (62.53ms, 10.3MB)
테스트 10 〉	실패 (시간 초과)
테스트 11 〉	실패 (시간 초과)
테스트 12 〉	실패 (시간 초과)
효율성  테스트
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	실패 (시간 초과)
'''


def solution(n):
    sqrt = int(n**(1/2))
    for i in range(sqrt):
        pass
    return 9**(1/2)  # len(prime)


print(solution(1000000))
