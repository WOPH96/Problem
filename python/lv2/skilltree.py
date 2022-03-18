def solution(skill, skill_trees):
    answer = len(skill_trees)

    # 아마 시간 초과 잘되네...?

    sk = [i for i in skill]
    # print(sk)

    for skills in skill_trees:
        n = 0
        # print(skills)
        for i in skills:
            if i in sk:
                if i == sk[n]:
                    # print(i)
                    n += 1
                else:
                    answer -= 1
                    break
        n = 0

    return answer
