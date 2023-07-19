import sys
sys.stdin = open('2003_input.txt','r')

n,m = map(int,input().split())
datas = list(map(int,input().split()))

'''
N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다. 이 수열의 i번째 수부터 j번째 수까지의 합 A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.
'''

'''
i부터 j까지 돌면서 해당하면 탈출, 카운트 증가
0은 데이터에 없으니 탈출해도 됨
--> 시간 초과
계속 했던거 더하지말고 DP테이블 생성
1+2+3 >m
2+3 = m
3+4 >m
4+2 >m
2+5 >m
5 =m
3+1+1=m
1+1+2<m

dp에 1~n까지 합 채운다

1 '2 3' 4  2  '5'  '3  1  1'  2
1  3 6 10 12  17   20 21 22  24

'1 '1' '1' 1'
1 2 3 4
뒤에서부터 24 23 21 18 14 12 7  4  3  2

순서상관없이 두개 차가 5인 것의 개수 구하기



'''

# cnt= 0
# for i in range(n):
#     sum = datas[i]
#     if sum==m:
#         cnt+=1
#         continue
#     for j in range(i+1,n):
#         sum+=datas[j]
#         if sum==m:
#             cnt+=1
#             break
# print(cnt)

'''
구간합 스킬 사용하라..
 l     r
1 '2 3' 4  2  '5'  '3  1  1'  2
l 값을 증가하면 구간합 감소
r 값을 증가하면 구간합 증가
l=r일수 있음
'''

left,right = 0,1
cnt = 0

while right<=n and left<=right:
    r_sum = sum(datas[left:right])
    
    if r_sum == m: #정확히 찾았으면
        cnt +=1 #카운트 증가 후 포인터이동
        left+=1
        right+=1
    elif r_sum < m:
        right+=1
    elif r_sum > m:
        left+=1
print(cnt)



    