def solution(s):
    answer = ''
    str = s.split(" ")
    print(str)
    for word in str:
        for i in range(len(word)):
            if i % 2 == 0:
                word[i] = word[i].upper()
    return answer


print(solution("try hello world"))
