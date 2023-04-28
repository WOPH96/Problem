import sys
sys.stdin = open('2579_input.txt', 'r')

n = int(input())

l = [int(input()) for _ in range(n)]

'''
최댓값 출력
i,i+1중에서 최댓값 저장
세개 연속 밟으면 안됨
마지막은 무조건 밟아야함
마지막에서 시작하면 되겠다

i, i+1, i+2 



'''
