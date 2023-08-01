import sys
# sys.stdin = open('43165_input.txt','r')


def solution(numbers, target):
    answer = 0
    length = len(numbers)

    def dfs(cnt, sum):
        nonlocal length
        nonlocal target
        nonlocal answer
        # 탈출
        if cnt == length:
            if sum == target:
                answer += 1
            return
        # 구현
        dfs(cnt+1, sum+numbers[cnt])
        dfs(cnt+1, sum-numbers[cnt])
    dfs(0, 0)

    return answer


print(solution([1, 1, 1, 1, 1], 3))  # 5
print(solution([4, 1, 2, 1], 4))  # 2
