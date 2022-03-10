def solution(s):
    answer = ''
    a = sorted(s, key=lambda word: ord(word), reverse=True)
    return "".join(a)


print(solution("Zbcdefg"))
print(solution("aBcDeFgH"))
