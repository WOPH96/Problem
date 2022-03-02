# def solutions(s):
#     answer = ''
#     str = s.split(" ")
#     for word in str:
#         for i in range(len(word)):
#             if i % 2 == 0:
#                 answer += word[i].upper()
#             else:
#                 answer += word[i]
#         answer += " "
#     return answer


def solution(s):
    answer = ''
    i = 0
    for word in s:
        if word == ' ':
            i = 0
            answer += word
        elif i % 2 == 0:
            answer += word.upper()
            i += 1
        elif i % 2 == 1:
            answer += word.lower()
            i += 1

    return answer


print(solution("try      hello world"))
