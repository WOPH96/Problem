import sys
sys.stdin = open('1436_input.txt','r')
'''
입력
첫째 줄에 N이 주어진다. N은 10,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 N번째 영화의 제목에 들어간 수를 출력한다.
'''

n = int(input())

'''
666이 문자열안에 들어가있으면 ok
'''
cnt = 0
for i in range(100000000):
    if '666' in str(i):
        cnt+=1
    if cnt==n:
        break
print(i)