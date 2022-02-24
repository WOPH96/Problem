def solution(x, n):
    if x>=0 :
        answer = [i for i in range(x,x*n+1,x)]
    else:
        answer = [i for i in range(x,x*n-1,x)]
    return answer


print(solution(-4,2))