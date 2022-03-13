def solution(absolutes, signs):
    answer = 0
    for i in range(len(signs)):
        if signs[i]:
            answer+=absolutes[i]
        else:
            answer+=-1*absolutes[i]
    return answer