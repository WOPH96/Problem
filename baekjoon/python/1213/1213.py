import sys
sys.stdin = open('1213_input.txt','r')

#첫째 줄에 문제의 정답을 출력한다. 만약 불가능할 때는 "I'm Sorry Hansoo"를 출력한다. 정답이 여러 개일 경우에는 사전순으로 앞서는 것을 출력한다.

'''
백트래킹 말고 알고리즘을 작성하자

ABAB
BAAB
ABBA

사전순으로 ABBA가 앞섬

문자받아서
정렬

다른 문자는 하나만 있어야함
나머지 다 짝수
총 26개

[A,A,A,A,B,B]
식으로 정렬
AABBAA
개수 카운팅 
A몇개 B몇개 C몇개 -- 이렇게 해서도 풀수있긴한데 뭔가안좋을듯
걍 카운팅ㄱㄱ 하고 다른 방법 서치

1. count=[0]*26 만들고 입력값 돌면서 카운팅 조지고
2. 홀수가 2개 이상이면 fail
3. 짝수만 있거나, 홀수 1개면 배치 ㄱㄱ
    4. stack에 삽입 result에 삽입
    5. 

'''

words = input()

count=[0]*26
result = ""
#print(words)

for word in words:
    idx = ord(word)-ord('A')
    count[idx]+=1

def check() -> bool:
    checking = list(map(lambda a : a%2,count)).count(1)
    if checking >= 2:        
        return False
    else :
        return True

if not check():
    print("I'm Sorry Hansoo")
else:
    stack = []
    idx = 0
    alpha_odd = ""
    for i,cnt in enumerate(count) : # 인덱스번호 / 횟수 
        if cnt == 0 :
            continue
        elif cnt%2==1:
            alpha_odd = chr(i+ord('A')) # alpha
            if cnt>1:
                stack.append(alpha_odd)
                result+=alpha_odd*int(cnt/2)
        else:
            alpha = chr(i+ord('A')) # alpha
            stack.append(alpha)
            result+=alpha*int(cnt/2)
    result+= alpha_odd
    while(stack):
        alpha = stack.pop()
        idx = ord(alpha)-ord('A')
        result+=alpha*int(count[idx]/2)
    print(result)