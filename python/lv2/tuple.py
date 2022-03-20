
def tointlist(s):
    answer = []
    flag = False

    i = 1
    num = -1
    # print(len(s)-1)
    while(i < len(s)-1):
        if not flag:
            if s[i] == ",":
                i += 1
                continue
            answer.append([])
            num += 1
        if s[i] == "{":
            flag = True
            i += 1
            continue
        elif s[i] == ",":
            i += 1
            continue
        elif s[i] == "}":
            flag = False

        if flag:
            answer[num].append(int(s[i]))
        i += 1
    return answer


def solution(s):
    st = set()
    s = tointlist(s)
    print(s)

    return st


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
