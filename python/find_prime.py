def solution(n):
    
    answer=0
    prime = [True]*(n+1) #prime[2] = True ==> 2는 소수
 
    sq = int(n**0.5) #2
    # 0 1 2 3 4
    # x f t t f
    for i in range(2,sq+1):
        if prime[i]==True:
            for j in range(i+i,n+1,i):
                prime[j]=False
    for i in prime[2:]:
        if i : answer+=1
    print(prime[2:])

    return answer
        
print(solution(2))
print(solution(5))
print(solution(10))