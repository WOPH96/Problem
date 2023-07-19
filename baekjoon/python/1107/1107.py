import sys
sys.stdin = open('1107_input.txt','r')

target = int(input())
M = int(input())
malf=[]
if M:
    malf = list(map(int,input().split()))
m = abs(target-100)
# print(malf)

'''
5457 가까운 수로 이동해야함
m = abs(target-100) 얘보다 작아야 다른 정답
678
5455 (4번) + 2 = 6
0~9 - malf 리스트 = 정상리스트
case 1. 정상 버튼으로 만들수 있는 것중에 가장 차이가 작은 것
case 2. 타겟 업다운 후 버튼 리스트 <<< 이걸로 하자


'''
total = list(range(10))
# print(total)
oks = [str(x) for x in total if x not in malf]
# print(oks)

# test
# tmp = target-2
# b = all(map(lambda a:a in oks,str(tmp)))
# print(b)


for cnt in range(0,500000):
    #한쪽은 빼기만해서
    minus = target-cnt
    check = all(map(lambda a:a in oks,str(minus)))
    if check : 
        target=minus
        break  
    #한쪽은 더하기만
    plus = target+cnt
    check = all(map(lambda a:a in oks,str(plus)))
    if check : 
        target=plus
        break      
    
    #ok로만 완성할 수 있으면 탈출
mv = cnt+len(str(target))
res = min(m,mv)
print(res)