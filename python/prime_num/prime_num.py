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


print(solution(10))
print(solution(5))
