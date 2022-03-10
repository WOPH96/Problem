def solution(dartResult):
    answer = 0
    ten_flag = False
    for info in dartResult:
        if ord('0') <= ord(info) <= ord('9'):
            num = int(info)
            if info == '1':
                ten_flag = True


return answer
