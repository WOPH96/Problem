def solution(x):
    #answer = True

    nb_sum = 0

    temp = x

    while temp != 0 :
        nb_sum += temp%10
        #print(nb_sum)
        temp //=10
        #print(temp)

    # if (x%nb_sum) == 0 :
    #     return True
    # else :
    #     return False

    return True if (x%nb_sum) ==0 else False

    #return answer

print(solution(1234))
print(solution(12))
print(solution(11))
print(solution(13))