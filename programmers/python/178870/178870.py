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
찾으면 두칸 다 앞으로

'''


def solution(sequence, k):
    answer = []
    return answer


solution([1, 2, 3, 4, 5],	7)  # [2, 3]
solution([1, 1, 1, 2, 3, 4, 5],	5)  # [6, 6]
solution([2, 2, 2, 2, 2],	6)  # [0, 2])
