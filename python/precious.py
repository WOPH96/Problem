from collections import deque

def tosharp(x,y):
    s=''
    for i in range(len(x)):
        if(x[i] or y[i]):
            s+='#'
        else:
            s+=' '
    return s

def tobinary(x,n):
    dq = deque()
    while x:
        dq.appendleft(x%2)
        x//=2
    
    for _ in range(n-len(dq)):
        dq.appendleft(0)
    
    return list(dq)
    
def solution(n, arr1, arr2):
    answer = []
    n= [n]*n
    #tobinary(arr1[1])
    a = list(map(tobinary,arr1,n))
    b = list(map(tobinary,arr2,n))
    answer = list(map(tosharp,a,b))
    #print(a)
    #print(b)
    #print(c)
    return answer