import sys
sys.stdin = open('7568_input.txt', 'r')
'''
입력
첫 줄에는 전체 사람의 수 N이 주어진다. 그리고 이어지는 N개의 줄에는 각 사람의 몸무게와 키를 나타내는 양의 정수 x와 y가 하나의 공백을 두고 각각 나타난다.

출력
여러분은 입력에 나열된 사람의 덩치 등수를 구해서 그 순서대로 첫 줄에 출력해야 한다. 단, 각 덩치 등수는 공백문자로 분리되어야 한다.
'''
n = int(input())
people = []
for _ in range(n):
    people.append(list(map(int, input().split())))
dungchi = [1]*n
for i in range(n):
    for j in range(i+1, n):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            dungchi[i] += 1  # 등수가 높을수록 덩치작은거
        elif people[i][0] > people[j][0] and people[i][1] > people[j][1]:
            dungchi[j] += 1
for d in dungchi:
    print(d, end=" ")
