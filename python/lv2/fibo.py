# def fibo(x,d):
#     if x<=2:
#         d[x] == 1
#         return 1

#     if d[x] == 0:
#         d[x] = fibo(x-2,d)+fibo(x-1,d)
#     return d[x]

def solution(n):
    answer = 0
    d = [0]*100001

    d[1] = 1
    d[2] = 1

    for i in range(2, n+1):
        if d[i] == 0:
            d[i] = d[i-2]+d[i-1]

    answer = d[n] % 1234567

    return answer
