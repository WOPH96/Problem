def func(students):
    ans = []
    mx = max(students)
    for i in range(len(students)):
        if students[i] == mx:
            ans.append(i+1)

    return ans


def solution(answers):

    answer = [0, 0, 0]
    supos = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    # print(answers)
    for i in range(len(supos)):
        supos[i] = supos[i]*(len(answers)//len(supos[i])+1)

    for i in range(len(answers)):
        if supos[0][i] == answers[i]:
            answer[0] += 1
        if supos[1][i] == answers[i]:
            answer[1] += 1
        if supos[2][i] == answers[i]:
            answer[2] += 1

    return func(answer)


print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))
