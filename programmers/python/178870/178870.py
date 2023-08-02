'''
#큰그림
찾으면 스택에 넣고
스택 맨 마지막값보다 작은 배열일때만 넣기
맨 위의 값 출력
이러면 작은 배열일때만 출력할 수 있음

#작은그림
left right 구성
00부터 시작
[left:right+1] 형식으로 list slicing
찾으면 두칸 다 한칸씩 앞으로
작으면 왼쪽만 한칸 앞으로
크면 오른쪽만 한칸 뒤로

right+1 > len 이거나 left>right이면 종료? 굿


'''


def solution(sequence, k):
    answer = []

    length = len(sequence)
    left = right = 0
    stack = []
    while right+1 <= length and left <= right and sequence[right] <= k:
        tot = sum(sequence[left:right+1])
        if tot == k:
            print(tot, left, right)
            if not stack:
                stack.append([left, right])
                if right-left == 0:
                    break
            else:
                gap = stack[-1][1]-stack[-1][0]
                if gap > right-left:
                    stack.append([left, right])
                    if right-left == 0:
                        break
            left += 1
            right += 1
        elif tot < k:
            right += 1
        elif tot > k:
            left += 1
    answer = stack[-1]
    print(answer)
    return answer


# solution([1, 2, 3, 4, 5],	7)  # [2, 3]
# solution([1, 1, 1, 2, 3, 4, 5],	5)  # [6, 6]
# solution([2, 2, 2, 2, 2],	6)  # [0, 2])
solution([1, 1, 1, 2, 3, 4, 5],	1)  # [0, 0]
