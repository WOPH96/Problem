import sys
sys.stdin = open('15683_input.txt','r')

'''
dfs -> 탐색
cctv위치 
cctv종류에 따른 mode
direction

'''

cctv=[]


dx=[0,1,0,-1] #
dy=[1,0,-1,0] #

mode=[
[],
[[0],[1],[2],[3]],
[],
[],
[],
[],
]