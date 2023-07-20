import sys
sys.stdin = open('15683_input.txt','r')

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

for elem in graph:
    print(elem)

'''
idea :
1 -> 4가지 (상하좌우)
2 -> 2가지 (위아래/양옆)
3 -> 4가지 (ㄱ모양 4가지)
4 -> 4가지 (ㅓ모양 4가지)
5 -> 1가지 

CCTV 최대 개수 8개 -> 4^8 =65,536이 최대 반복횟수 -> 완전탐색 

1. 0을 제외한 모든 위치 저장 후
2. 5->4->3->2->1 순서로 시야 방사, 감시된 곳은 7로 변경하기
-> 1. 시야는 벽이거나, 6이면 막힘
-> 2. 어짜피 위치는 저장돼있으니 6제외하곤 다 7로 만들기
-> 3. 카메라 타입 받아서 이동방향 dx dy으로 설정하면 되지 않을까 ..
'''

Positions=[[] for _ in range(7)]

#1. 0을 제외한 모든 위치 저장
for i in range(n):
    for j in range(m):
        if 0<graph[i][j]<=6:
            Positions[graph[i][j]].append((i,j))

for elem in Positions:
    print(elem)

def view(c_type:int) -> tuple:
    if c_type==1: # 1번 카메라라면  
        pass

# 있는 카메라 대상으로만 돌리고 싶은데..
camera_available =[0]*7
for i,camera in enumerate(Positions):
    if camera:
        camera_available[i]=1
print(camera_available)

#각 카메라의 경우의 수
prob={1:4,2:2,3:4,4:4,5:1}

from itertools import product

for elem in product(list(range(prob[1])),repeat=len(Positions[1])): 
    #print(elem)
    pass

'''
8개가 전부 방향을 정하는게 1턴
viewed = set()
1이 있는가? yes
6개 -> 4^6 패턴 나와야 함
view(c_type:int,position:list,pattern:tuple) -> 방사된좌표들 리턴
viewed.append (리턴좌표들)
2가있는가? no
..
5가 있는가? yes
view(c_type,pattern) -> 방사좌표 리턴

있는거만 진행
1,5


'''
avail = sum(camera_available)

for _ in range(avail):
