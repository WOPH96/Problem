import sys
sys.stdin = open('15683_input.txt','r')

'''
dfs로 모든 경우의 수를 돌게끔 설정
경우 1
1부터 n번째 카메라
경우 2
1부터 n번째 카메라

for 경우의 수 
dfs(카메라)

정답지와 동일하게 코딩하는 연습
출처 : https://developer-ellen.tistory.com/53

생각하면서

'''

N,M = map(int,input().split())

#모든 맵 정보
graph=[]

#CCTV 종류/(x좌표,y좌표)
cctv = []

#그래프 입력받으면서 cctv 좌표도 입력받기
for i in range(N):
    #한줄입력완료
    graph.append(list(map(int,input().split())))
    
    #그 줄에서 cctv위치 저장 (종류/(x,y)좌표)
    for j in range(M):
        # 카메라 종류라면
        if 0<graph[i][j]<6:
            cctv.append([graph[i][j],i,j])
# print(cctv)

#CCTV 종류에 따른 방사방법
mode=[
[],#비워둠
[[0],[1],[2],[3]], # 1번카메라 - r/l/d/u
[[0,1],[2,3]], #2번카메라 - rl/du
[[0,3],[1,2],[1,3],[2,3]], #3번카메라 - ru/ul/ld/dr
[[0,1,2],[0,1,3],[0,2,3],[1,2,3]],#4번카메라 rul,uld,ldr,urd
[[0,1,2,3]],#5번카메라 rldu
]

#CCTV 방사방향 
#   r l d u
dx=[0,0,1,-1] # 1=아래, -1=위
dy=[1,-1,0,0] # 1=오른쪽, -1=왼쪽


#원본 그래프는 건드리면 계산에 문제 생길 수 있음
from copy import deepcopy

#해당 경우에 속하는 감시경로 ㄱㄱ, 채운 곳은 7로 한다
def fill(temp_graph,x,y,direction):
    for i in direction: # 만약 2번 카메라라면, 0번 경우에 대해 0,1 방향으로 쏴야함
        # x,y는 기준점이 되어야 하니 고정
        filled_x = x
        filled_y = y
        while True:
            # 그 방향으로 쭉 직진한다
            filled_x+=dx[i]
            filled_y+=dy[i]
            #현위치가 틀에 부딪혔다면 -> 현위치가 틀 내부가 아니라면 -> 종료
            if not(0<=filled_x<N and 0<=filled_y<M):
                break
            #현위치가 벽에 부딪혔다면 -> 종료
            if temp_graph[filled_x][filled_y] == 6: # or elif 상관없음, 어짜피 위에 break니까
                break
            #현위치가 빈공간이라면 -> 7로 채우기
            elif temp_graph[filled_x][filled_y] == 0:
                temp_graph[filled_x][filled_y] = 7
            #현위치가 다른 cctv인 경우엔 아무것도 하지 않는다

#모든 CCTV의 모든 경우 체크
def dfs(depth,arr): # n번쨰 카메라인지 확인 / 한 경우에 모든 카메라를 다 돌아야 함, dfs를 경우의 수 반복문 안에 넣는다
    global m
    if depth == len(cctv): # 모든 카메라 돌았다면 
        #해당 경우에 대한 사각지대 최솟값 구해야함
        cnt = sum(map(lambda x:x.count(0),arr))
        m = min(m,cnt)
        return 0
    
    #depth번째 cctv의 정보 받기
    cctv_num, x,y = cctv[depth]
    
    #원본정보 유지하고 매 경우마다 리프레쉬
    temp_graph = deepcopy(arr)
    #해당 cctv의 경우의 수 반복하기
    for i in mode[cctv_num]:
        #해당 cctv의 i번째 경우 카메라 비추기
        fill(temp_graph,x,y,i)
        #다음 카메라 ㄱㄱ
        dfs(depth+1,temp_graph)
        #모든 경우에 대한 카메라에 대한 정리가 끝났으면, 다시 원본 그래프로 변경하여 새로운 경우 진입
        temp_graph = deepcopy(arr)
m=N*M #전체 맵 크기보단 작지
dfs(0,graph) # 처음 카메라부터 시작, 원본 그래프 전달
print(m)