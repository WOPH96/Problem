def solution(s, n):
    answer = ''
    for spell in s:
        tmp = ord(spell)+n
        if ord(spell)==32:
            answer+=spell
        elif ord('A')<=ord(spell)<=ord('Z') and tmp > ord('Z'):
            answer+=chr(ord('A')+tmp-ord('Z')-1)
        elif ord('a')<=ord(spell)<=ord('z') and tmp > ord('z'):
            answer+=chr(ord('a')+tmp-ord('z')-1)
        else:
            answer+=chr(tmp)
    return answer

print(solution("AB",1))
print(solution("z",1))
print(solution("a B z",4))

