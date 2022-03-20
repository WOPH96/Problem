def solution(sizes):
    answer = 0
    trans = list(map(list, zip(*sizes)))
    print(trans)

    mx = [max(trans[0]), max(trans[1])]
    M = mx.index(max(mx))
    m = m = M ^ 1

    while True:
        idx = trans[m].index(mx[m])  # 작은놈의 맥스 위치
        Maxidx = trans[M].index(mx[M])
        if trans[m][idx] <= trans[M][idx]:  # 짝보다 작으면
            break
        trans[m][idx], trans[M][idx] = trans[M][idx], trans[m][idx]  # 짝보다 크면 스왑
        mx[m] = max(trans[m])

    return mx[0]*mx[1]
