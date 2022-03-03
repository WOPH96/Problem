def solution(s):
    answer = True
    cnt = 0
    for ch in s:
        if ch is 'p' or ch is 'P':
            cnt += 1
        elif ch is 'y' or ch is 'Y':
            cnt -= 1
    return True if cnt == 0 else False


print(solution("pPoooyY"))
