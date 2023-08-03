import sys
sys.stdin = open('5014_input.txt','r')

# top_floor, current_floor, target_floor, Up, Down
tf,cf,tf,u,d = map(int,input().split())

# fail_comment 
fc = "use the stairs"

print(tf,cf,tf,u,d)

'''
target - curent = 움직여야 하는 수
gap = 10-1 = 9 

+u와 -d로 gap을 최소로 만들려면..
많은 값 8-1+2
dfs 하기전에
근접까진 해놓자

if gap > 0
(gap-u)//u

gap = 1 - 10 = -9
if gap < 0
(gap+d)//d

'''
btn = 0
gap = tf - cf
if gap >0:
    btn = (gap-u)//u
    gap = (gap)%u+u
    print(btn,gap)
elif gap <0:
    btn = (gap+d)//d
    gap = (gap)%d-d
    print(btn,gap)
else:
    print(0)
    exit

