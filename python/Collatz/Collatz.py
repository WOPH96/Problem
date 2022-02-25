def solution(num):
    answer =0
    if num==1:
        return 0
    while(answer<=500):
        if num%2==0:
            num//=2
            answer+=1
        else:
            num=num*3+1
            answer+=1
        if num == 1: 
            break


    return -1 if answer>500 else answer


print(solution(1))
print(solution(16))
print(solution(626331))