import sys
sys.stdin = open('11000_input.txt','r')
'''
13 35
24 
2개

시작/종료


'''
classes = []
n= int(input())
for _ in range(n):
    a,b= map(int,sys.stdin.readline().split())
    classes.append([a,b])
classes.sort() # 시작시간으로 정렬

# 끝나는 시간을 기준으로 우선순위 큐
import heapq as hq

room = []
hq.heappush(room,classes[0][1]) # 제일 빨리 끝나는 시간이 맨위 

for i in range(1,n):
    if classes[i][0]<room[0] :  # 시작시간 < 제일 빨리 끝나는 수업 
        # - 룸 새로 생성
        hq.heappush(room,classes[i][1]) 
    else: # 시작시간 > 제일빨리끝나는 방 : 기존 방 쓰면 되니 
        #빨리 끝나는 수업 제거 후 방금 들어간 클래스 삽입
        hq.heappop(room)
        hq.heappush(room,classes[i][1])

print(len(room))

