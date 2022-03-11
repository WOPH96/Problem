def solution(a, b):
    answer = ''
    days = 0
    day = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(a):
        days += day[i]
    days += b-1
    YOIL = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    answer = YOIL[days % 7]
    return answer


print(solution(1, 2))
